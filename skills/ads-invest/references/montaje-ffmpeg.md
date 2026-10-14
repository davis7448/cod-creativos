# Montaje con ffmpeg y subida a Meta

Montaje sin escribir código: solo bash + ffmpeg. Probado en rondas reales de 4 videos por producto (19–23 s cada uno, 9:16).

## Insumos por video
- Voz validada: `voz/vo_XX.wav` · música: `musica/music_XX.wav` (al 0,15) · subtítulos PNG 1080×1920 transparentes: `caps/XX_NN.png` · tarjeta final: `clips/card_oferta.png`.
- `SC=("tipo|archivo|inicio|fin" …)` con un corte al inicio de cada frase de la voz:
  - `v`: clip del proveedor (horizontal o cuadrado) → fondo difuminado + clip encima, subido 80 px.
  - `f`: clip ya preparado a 1080×1920 → pantalla completa (stock vertical, o clip de fábrica ya compuesto, ver abajo).
  - `i`: imagen 1080×1920 (Codex, landing, tarjeta) → zoompan suave hasta 1,12.
- **Clips de fábrica horizontales (720p): NO recortarlos a 9:16.** Recortar una franja vertical de un video de 1280×720 lo amplía ~2,7× y se ve borroso y demasiado cerrado (queja real del usuario: "tienen mucho zoom"). Lo que funcionó: un **cuadrado** de 640–720 px alrededor de la acción, escalado a 1080×1080 (1,5×) sobre la misma toma difuminada, y tratarlo como `f`:
  ```bash
  sq(){ ffmpeg -nostdin -v error -y -ss $3 -t $4 -i $2 -filter_complex "[0:v]crop=$5,scale=1080:1080,setsar=1,split[s][b];[b]scale=1920:1920,crop=1080:1920,boxblur=30:3,eq=brightness=-0.05[bg];[bg][s]overlay=0:380,fps=30,format=yuv420p" -an -c:v libx264 -crf 18 clips/$1.mp4; }
  sq fa_nino_taladro fabrica.mp4 11.35 2.8 720:720:150:0   # nombre fuente inicio duración crop(w:h:x:y)
  ```
  Con texto chino quemado abajo, sube el cuadrado (`crop=590:590:x:0`) para dejarlo fuera.
- **Menos imágenes fijas:** el usuario rechazó videos "con muchas fotos" y stock fuera de contexto. Prioridad: tomas de fábrica en movimiento > stock que coincide con la frase > imágenes de la landing (solo la tarjeta final).
- `CP=("inicio|fin[|índice]" …)`: un subtítulo por bloque. El índice es opcional y sirve cuando el PNG no sigue el orden.

## Función build (copiar tal cual dentro de `bash <<'EOF' … EOF`, desde la carpeta de la ronda)
```bash
L=../landing; R=broll
build(){ out=$1; vo=$2; mu=$3; name=$4; ins=""; fc=""; n=0; cat=""
 for s in "${SC[@]}"; do IFS='|' read -r t f a b <<<"$s"; d=$(printf "%.3f" $(echo "$b-$a"|bc))
  if [ "$t" = v ]; then ins="$ins -stream_loop -1 -t $d -i $f"
   fc="$fc[${n}:v]split[a${n}][b${n}];[a${n}]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=25:2[bg${n}];[b${n}]scale=1080:-2[fg${n}];[bg${n}][fg${n}]overlay=(W-w)/2:(H-h)/2-80,setsar=1,fps=30,trim=0:${d},setpts=PTS-STARTPTS,format=yuv420p[v${n}];"
  elif [ "$t" = f ]; then ins="$ins -stream_loop -1 -t $d -i $f"
   fc="$fc[${n}:v]scale=1080:1920,setsar=1,fps=30,trim=0:${d},setpts=PTS-STARTPTS,format=yuv420p[v${n}];"
  else ins="$ins -loop 1 -t $d -i $f"
   fc="$fc[${n}:v]scale=1080:1920,setsar=1,fps=30,trim=0:${d},setpts=PTS-STARTPTS,zoompan=z='min(zoom+0.0012,1.12)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=30,format=yuv420p[v${n}];"
  fi; cat="$cat[v${n}]"; n=$((n+1)); total=$b; done
 fc="$fc${cat}concat=n=${n}:v=1:a=0[base];"; prev=base; i=0
 for c in "${CP[@]}"; do IFS='|' read -r a b k <<<"$c"; b2=$(printf "%.3f" $(echo "$b-0.04"|bc)); idx=$((n+i)); f=$(printf "caps/%s_%02d.png" $out ${k:-$i}); ins="$ins -i $f"
  fc="$fc[$prev][${idx}:v]overlay=0:0:enable='between(t,${a},${b2})'[c${i}];"; prev=c${i}; i=$((i+1)); done
 vi=$((n+i)); mi=$((vi+1)); ins="$ins -i $vo -i $mu"
 fc="$fc[${vi}:a]apad,atrim=0:${total}[vo];[${mi}:a]atrim=0:${total},volume=0.15,afade=t=out:st=$(echo "$total-1"|bc):d=1[mu];[vo][mu]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[aout]"
 ffmpeg -nostdin -v error -y $ins -filter_complex "$fc" -map "[$prev]" -map "[aout]" -c:v libx264 -crf 20 -pix_fmt yuv420p -c:a aac -b:a 192k -ac 2 -ar 48000 -t $total -movflags +faststart "final/con_voz/$name.mp4" && echo "LISTO $name"
}
# Ejemplo (MM04, con stock):
SC=("f|clips/stk_nina_regalo.mp4|0|2.68" "f|clips/stk_mujer_sorpresa.mp4|2.68|4.24" "v|clips/v1_set6.mp4|4.24|5.36" "i|$R/b01_mano_corazones.png|5.36|7.18" … "i|clips/card_oferta.png|17.46|19.5")
CP=("0|.82" ".82|1.7" … "13.0|13.72|18" …)
build MM04 voz/vo_MM04.wav musica/music_MM04.wav MM_VN04_regalo_navidad_CON_VOZ
```
- `-nostdin` es obligatorio (sin él, ffmpeg se come el heredoc). `printf "%.3f"` evita decimales como `.96` que ffmpeg no lee.
- Antes de rearmar: respaldar la versión anterior en `final/con_voz/v1_<origen>/`.

## QA
- Duración de cada mp4 = fin de la última escena.
- Un fotograma en el centro de cada escena nueva (`-ss t -frames:v 1 -vf scale=216:384` → `hstack`): revisar que **la imagen coincida con el subtítulo** y que el producto no esté deformado.
- Si se cambió la voz: transcribir con whisper y comparar con el guion. Si solo cambió la imagen, el audio queda igual.

## Subida a Meta (después del ok del usuario)
IDs (cuenta, página, Instagram, píxel, país): de `CONFIG-TIENDA.md`.
1. **Miniatura propia por video:** `ffmpeg -ss 0.5 -i X.mp4 -frames:v 1 -q:v 2 thumb_X.jpg` (el gancho con su subtítulo).
2. **URL pública vía Shopify Files:** `stagedUploadsCreate` (resource FILE, mp4 y jpg en una sola llamada, con `fileSize`) → POST multipart con `curl -F` por cada destino (los parámetros en el orden recibido y `file=@…` al final; esperar 201) → `fileCreate` con los `resourceUrl` → `nodes(ids)` hasta `READY` para leer `url` (cdn.shopify.com). Para no copiar firmas a mano: leer la respuesta desde el jsonl de la sesión (`~/.claude/projects/<proyecto>/<sesión>.jsonl`), filtrando las líneas con `x-goog-signature` que no contengan `python3`.
3. `ads_creative_upload_media` (URL, VIDEO para el mp4 · IMAGE para la miniatura → `hash`) → `ads_get_ad_videos` con `video_ids` hasta `status` listo.
4. `ads_create_ad_set` (un conjunto OPEN por video): `OFFSITE_CONVERSIONS`, `IMPRESSIONS`, `WEBSITE`, `promoted_object={"pixel_id":"<PIXEL_ID>","custom_event_type":"PURCHASE"}`, `targeting={"geo_locations":{"countries":["<CC>"]},"age_min":18,"age_max":65}`, sin presupuesto (la campaña es CBO).
5. `ads_create_creative`: `video_id` + `image_hash` de su miniatura + `instagram_user_id` + `SHOP_NOW` + `link_url` con `utm_content=vn0X` + DOF con estas 9 funciones en OPT_OUT: `image_touchups, text_optimizations, adapt_to_placement, image_templates, image_uncrop, enhance_cta, product_extensions, site_extensions, video_auto_crop`. (`standard_enhancements` ya no se acepta).
6. `ads_create_ad` con `{"creative_id":…}` → `ads_get_ad_entities` con `object_state=draft` → `ads_activate_entity` con `object_ids` (conjuntos + anuncios) y `publish_as_active=true` → verificar estados en vivo y la vista previa.

**Campaña CBO ya publicada:** `ads_create_ad_set` responde "the parent campaign does not use CBO" aunque la campaña sí tenga presupuesto, porque valida contra el borrador. Arreglo probado: `ads_update_entity` en la campaña con el **mismo** `daily_budget` (no pausa nada) → crear conjuntos, creativos y anuncios → `ads_get_ad_entities` con `object_state=draft` → `ads_activate_entity` con la campaña, los conjuntos y los anuncios en `object_ids` y `publish_as_active=true`. Los anuncios pasan a ACTIVE / IN_PROCESS (revisión de Meta).

**Permisos:** el clasificador del modo automático puede bloquear `ads_creative_upload_media` y las llamadas que crean o activan objetos en Meta. En ese caso, parar y pedirle al usuario que agregue las reglas de permitir con `/permissions` (`mcp__claude_ai_Facebook__ads_creative_upload_media`, `ads_create_ad_set`, `ads_create_creative`, `ads_create_ad`, `ads_activate_entity`). No reintentar en bucle.
