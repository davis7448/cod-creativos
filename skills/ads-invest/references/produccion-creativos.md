# Producción de creativos propios (Regla 5)

**Material permitido (no negociable):** fotos y videos del proveedor o la fábrica (Drive, Shopify, galería de AliExpress del SKU exacto) + escenas generadas con Codex + **stock licenciado** (el de `CONFIG-TIENDA.md`) + material grabado por el usuario. **Nunca** pautar ni usar como b-roll videos de competidores o creadores, aunque el usuario lo pida. Alternativas: (1) videos del proveedor con el guion de la referencia, (2) que el usuario grabe una unidad con guion toma por toma, (3) licenciar al creador (los de "colaboración pagada" suelen aceptar).

## 1. Guion
- Cada video copia la **estructura** de UNA referencia (gemelo o top): transcribe con whisper → adapta a los claims ✅ de `PRODUCTO.md`.
- Léxico natural del país de la tienda, números escritos con letras y precios reales. Sin "antes" ficticio.
- Cada guion lleva su **avatar** (quién habla: edad, región, personalidad, dónde se graba) y se escribe como habla esa persona: de corrido, narrando lo que muestra, no como ficha técnica.
- Guiones, voz y escenas por video en `<producto>/media/ronda-a-<producto>/GUIONES-RONDA-A.md` (tabla: video · ángulo · voz · instruct/speed; guion; escenas; estado).
- **Dos formatos que ganan en productos COD:** (a) testimonio en primera persona (mamá/papá/cliente) y (b) macro sin voz de 7–11 s con texto en pantalla y música.

## 2. Voz — un avatar, una voz (VoxCPM2)
- **Motor recomendado: VoxCPM2** con el método de [voces-voxcpm2.md](voces-voxcpm2.md): ficha del avatar → guion UGC de corrido → voz base diseñada por descripción (acento y personalidad del avatar) → actuación frase por frase clonando esa voz → pausas a mano → sonido de celular. Meta medible: ≤ 6 pausas/min y ≥ 17 semitonos de rango, como un creador real.
- Lo de abajo es el respaldo con OmniVoice.

### Respaldo — OmniVoice
- Instalación, API, etiquetas válidas, errores conocidos y validación: [voces-omnivoice.md](voces-omnivoice.md).
- **Guion completo en UNA sola llamada** con `instruct` + `speed`. Así la voz no cambia a mitad del video.
- **Nunca `teenager`**: sale vacío o con un pito. Para una voz juvenil: `female, young adult, moderate pitch`, `speed` 1,1–1,15.
- Perfiles base (ajusta y guarda los aprobados en `CONFIG-TIENDA.md`): A curiosidad (female, young adult, high pitch, 1,12–1,15) · B presentadora (female, young adult, moderate, 1,0) · C estudiante (female, young adult, moderate, 1,12) · D mamá (female, middle-aged, moderate, 1,0) · E profe (female, young adult, low, 1,02) · F hombre (male, young adult, moderate, 1,05–1,15).
- **Validación obligatoria:** whisper transcribe la toma y se compara con el guion (difflib sobre texto normalizado). Si la similitud es < 0,9, se regenera. Revisa también que los **números** salgan de corrido (ver voces-omnivoice.md).
- Lo que no funcionó en pruebas reales: generar frase por frase (cada llamada es otra persona) y forzar "acento local" con léxico. Las voces neuronales gratuitas de Microsoft (edge-tts) no tienen licencia comercial.
- **No se clona la voz de ningún creador.** Para clonar hace falta una muestra de 15–30 s de alguien que lo autorice por escrito.

## 3. Tiempos por palabra
`mlx_whisper.transcribe(wav, path_or_hf_repo='mlx-community/whisper-large-v3-turbo', word_timestamps=True, language='es')` → lista `(palabra, inicio, fin)`. Los cortes de escena van al inicio de cada frase y los subtítulos en bloques de 3–4 palabras.

## 4. Música propia (sin derechos de terceros)
`~/.venvs/voz/bin/python -I <plugin>/skills/ads-invest/scripts/gen_music.py <preset> <seg> <salida.wav>` (presets: energetic, energetic108, ugc, ambient, warm, driving, tense, cinematic). Va a un volumen de 0,10–0,20 bajo la voz.

## 5. Material del proveedor (recortes)
- Hoja de miniaturas por video: `fps=12/<dur>,scale=240:-2,tile=6x2` → descartar tomas con letras chinas, otra marca o **otra versión del producto** (otro color de caja, otra herramienta).
- Clips horizontales de 720p: **no** recortarlos a una franja 9:16 (quedan ampliados ~2,7× y borrosos). Usa el cuadrado sobre fondo difuminado de [montaje-ffmpeg.md](montaje-ffmpeg.md).
- Clips cortos (2–5 s) con nombre descriptivo en `ronda-a-<producto>/clips/` (`fa_nino_mesa`, `fa_macro`, `v1_flor_creciendo`…).

## 6. Edición
- Solo ffmpeg + PNG renderizados en Playwright (`page.context().newPage()` + `setContent` + `screenshot`, fondo transparente con `omitBackground`): subtítulos por bloque, gancho y **tarjeta final de oferta 1080×1920** (producto + precios de los packs + "Envío gratis · Pagas al recibir" + CTA). **La función `build` completa está en `montaje-ffmpeg.md`.**
- Edición por guion: mide la referencia (cortes, tempo, fotogramas). UGC = cortes secos; explicativos = flechas y círculos.
- En títulos dentro del PNG: verifica que no se partan en dos líneas encima de la foto (`white-space:nowrap` + tamaño ajustado).

## 7. B-roll de stock (escenas de contexto)
- Ejemplo con Magnific/Freepik (MCP): `stock_search` con `content_type: video`, `orientation: portrait` y la consulta en inglés ("bored student studying notebook", "father and son building at home"). Revisa en el plan del usuario si el stock premium gasta créditos; **generar video con IA desde el MCP sí cobra**: si el usuario tiene modelos ilimitados en la app, Claude arma el Space y el usuario genera ([video-ia-spaces.md](video-ia-spaces.md)).
- Elegir: bajar las miniaturas a una carpeta propia y armar una hoja con `xstack` (en zsh se escribe `${i}` y no `$i:` dentro del filtro). Después, 8 fotogramas por clip para escoger el tramo.
- Descargar: `stock_download` (`type: video`, `max_bytes: 20000000`) → `curl` → recortar a `clips/stk_<escena>.mp4` con `-ss <inicio> -t 4 -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,setsar=1" -an`.
- **Regla de oro:** el stock no trae el producto. Solo va en escenas de contexto (problema, persona, emoción, regalo). Si en esa frase la voz nombra el producto, la escena lleva material del proveedor. Y el stock tiene que **coincidir con la frase**: un obrero con casco sobre fondo de color bajo "el taladro de papá" se rechazó por fuera de contexto.

## 8. Escenas con Codex (si falta material)
`codex exec --skip-git-repo-check -s workspace-write -C <dir> -i ref1 -i ref2 -- "Use your image generation tool… copy the generated image into the current working directory as X.png" >/dev/null 2>&1`. El producto SIEMPRE fiel a la foto real. Varias en paralelo con `&` + `wait`.
- Si el video tiene que mostrar el producto **en movimiento** (cómo se pone, cómo funciona) y el proveedor no trae esa toma, las imágenes de Codex sirven de primer fotograma para clips con IA en Magnific Spaces: [video-ia-spaces.md](video-ia-spaces.md).

## 8b. Estáticos (sin escribir HTML a disco)
- Se componen en el navegador: un servidor local de la carpeta de medios (`npx -y http-server <media> -p <puerto> -s` en segundo plano) y, en Playwright, `document.open(); document.write(html); document.close()` con las imágenes por ruta relativa → `page.screenshot` a 1080×1350 (4:5) y 1080×1920 (9:16, con los 340 px de abajo libres). Así no hace falta guardar archivos HTML (que un arnés puede bloquear).
- **Cada estático sale en las dos medidas** y van juntos en un solo anuncio (4:5 al feed, 9:16 a historias y reels): ver `montaje-ffmpeg.md` § Subida.
- Subtítulos de video transparentes con el mismo truco y `omitBackground: true`.
- **Los formatos nativos tienen que parecer la interfaz real** (corrección real: "el de noticia no parece noticiero"). Noticia = nota de portal: cabecera con un nombre de portal **inventado** (nunca un medio real), menú y lupa, barra de secciones, titular en letra de periódico (serif), autor y "2 min de lectura", foto con pie de foto que explique el mecanismo, un párrafo y el precio con "Ver más →". Lo mismo con historia de IG, WhatsApp o Google: si no se confunde con la app de verdad, no sirve.
- **Encuadre de las fotos** (corrección real: "las fotos están mal encuadradas"): en cada recuadro se ve completo lo que el texto nombra (la cara entera con las manos poniéndose el producto, el control completo con su pantalla). Ajusta `object-position` por foto y revisa que el precio o la píldora no tapen el último paso en la versión 9:16.
- Antes de mostrarlos: una hoja con todos en miniatura (`hstack`/`vstack`) y la **prueba de los 2 segundos** de la Regla 4b: producto visible + línea de mecanismo + beneficio en cada pieza. Errores vistos: la tarjeta del producto tapando la píldora de envío, texto quemado de otra imagen asomándose en un recorte y espacio en blanco al final de una tabla.

## 9. QA y entrega
- Fotogramas en el centro de cada escena: producto sin deformar, imagen que coincide con el subtítulo, voz sin claims ❌, **uso correcto** del producto (la IA puso a una profe escribiendo con marcadores de papel en un tablero → falso).
- Entrega: `<producto>/media/ronda-a-<producto>/final/<PREFIJO>_VN0X_<angulo>.mp4` + `INDEX-CREATIVOS.md`. Antes de subir, **mostrarle los videos al usuario** (`open <mp4>`) y esperar su ok. Respaldar cada versión anterior en `final/v1_<motivo>/`.
- Subida a Meta **solo por API** (`montaje-ffmpeg.md` § Subida). Nunca abrir el borrador en el editor de Ads Manager: en campañas de Ventas puede convertirlo a anuncio de catálogo.

## 10. Procesos largos (OmniVoice + whisper)
- Correr en segundo plano con `python -u` y una línea por pieza; vigilarlo con Monitor (`grep --line-buffered "LISTO|Error|Traceback"`).
- Para validar, `whisper-small-mlx` (rápido); `large-v3-turbo` solo para los tiempos finales.
- En Macs de 8 GB: no correr OmniVoice, whisper y el navegador a la vez (ver voces-omnivoice.md).
