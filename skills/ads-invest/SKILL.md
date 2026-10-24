---
name: ads-invest
description: Investiga anuncios de competidores en la Meta Ad Library, TikTok y AliExpress para productos de e-commerce contraentrega, y produce bancos de creativos, ángulos, ofertas, matrices de testeo y videos propios con voz listos para cargar en Meta. Úsala SIEMPRE que el usuario pida investigar competidores, buscar anuncios ganadores, analizar la biblioteca de anuncios / Ad Library, traer creativos de referencia, armar inspiración para campañas, decidir qué creativos testear, hacer videos o voces para anuncios, o continuar/siguiente ronda de investigación de un producto. Actívala aunque no diga "Ad Library" si habla de espiar competencia publicitaria, swipe file, anuncios que escalan, o cargar creativos para testear.
---

# Investigación de creativos y competidores (Meta Ad Library)

Esta skill captura el método para investigar publicidad de competidores y convertirla en material accionable: bancos de creativos de referencia, bancos de ángulos/ganchos, bancos de oferta, matrices de testeo y videos propios para cargar campañas en Meta. **Toda investigación termina en la INVESTIGACIÓN CREATIVA COMPLETA (Regla 4)**: público, dolores, niveles de conciencia, ángulos, estructura de landing, oferta, claims, competidores, copy, testeo, economía y todos los links, en un solo Artifact.

## ⚙️ Configuración de la tienda (leer SIEMPRE primero)

Toda la información de la tienda vive en **`CONFIG-TIENDA.md`**, en la carpeta de trabajo (por defecto `~/ads-invest/CONFIG-TIENDA.md`).
- Si no existe, **corre primero la skill `setup-creativos`** (o pídele al usuario los datos y créalo con la plantilla `templates/CONFIG-TIENDA.md` del plugin). No inventes IDs.
- De ahí salen: carpeta de trabajo, marca, país y moneda, dominio y tienda de Shopify, IDs de Meta (cuenta, página, Instagram, píxel), flete, tasas de despacho y entrega, material permitido (stock), voces aprobadas y preferencias del usuario.
- En este documento, `<PAIS>`, `<MONEDA>`, `<CARPETA>`, `<MARCA>`, etc. se refieren a los valores de ese archivo. Los ejemplos con Colombia/COP son casos reales de campo: adáptalos al país configurado.
- Cuando el usuario corrija algo o fije una preferencia ("no uses X", "siempre Y"), anótalo en la sección **Preferencias** de `CONFIG-TIENDA.md`.

## Carpeta de trabajo: `<CARPETA>` (por defecto `~/ads-invest`)

Todo el output va aquí salvo que el usuario indique otra ruta. Estructura recomendada (un documento por tipo y por producto; cada ronda se AÑADE, no se crean archivos por ronda):
```
<CARPETA>/
├── CONFIG-TIENDA.md                ← datos de la tienda y preferencias (setup-creativos)
├── INICIO.md                       ← índice maestro del vault (Obsidian)
├── REGISTRO-INVESTIGACION.md       ← índice maestro de cobertura (leer SIEMPRE primero)
├── <producto-1>/
│   ├── PRODUCTO.md                 ← ⭐ ficha VERIFICADA del producto (specs, mecanismo, claims sí/no, precio, economía)
│   ├── COPY.md                     ← copy completo de cada anuncio
│   ├── BANCO-ANGULOS.md            ← ⭐ ángulos + ofertas + plan de testeo
│   ├── RANKING.md                  ← competidores ordenados mejor→peor
│   ├── ANALISIS-BIBLIOTECAS.md     ← por competidor: qué copiar / qué ignorar
│   ├── INDEX-CREATIVOS.md          ← ficha de cada creativo descargado
│   └── media/                      ← archivos .mp4 / .jpg descargados
└── <producto-2>/ ...
```
Si la carpeta no existe, créala. Conecta los documentos con wikilinks `[[ ]]` de Obsidian y enlázalos desde `INICIO.md`.

## ⭐ REGLA 0 — Verificar el producto REAL antes de buscar (no negociable)

Nunca investigues sobre un producto supuesto. En una ronda real se perdió una investigación entera por asumir "plantilla de comodidad" cuando el producto era una plantilla correctora de 3/4 en TPR.

1. Consigue la fuente del producto: link de Shopify, carpeta de Drive o fotos del usuario.
2. **Si es una carpeta de Drive y la API no lista archivos**, lístala en el navegador y descarga sin navegador (`drive.usercontent.google.com/download?id=<id>&export=download&confirm=t`); los .docx se leen con `unzip -p f.docx word/document.xml`. Detalle: [references/tecnico-busqueda.md](references/tecnico-busqueda.md). Revisa todos los videos del proveedor: alguno puede traer otra marca en la caja o ser **otra versión** del producto.
2b. **¿El nombre comercial ya está tomado?** Antes de bautizar el producto, busca el nombre en Meta/TikTok/Google: si en el mercado ya significa otro producto, el anuncio y la landing confunden (ej.: "marcadores mágicos" en LATAM = los que cambian de color → se usó "Marcadores Mágicos **de Figuras**"). Anótalo en `PRODUCTO.md`.
3. Escribe `PRODUCTO.md` con: formato, material, tallas o presentaciones, mecanismo, lo que promete el proveedor, la tabla de **claims ❌ no / ✅ sí**, el lenguaje visual del proveedor (qué foto sirve para qué) y el precio y costo si se conocen.
4. **No marques a nadie como "gemelo" sin verificarlo visualmente** (miniatura del creativo contra las fotos del producto). Si no hay gemelo, dilo explícitamente.
5. Si no puedes ver el producto, **pregunta antes de buscar**. No supongas.

## ⭐ REGLA 0d — Mercado local: ¿quién lo vende ya en `<PAIS>` y a qué precio? (siempre, antes de fijar la oferta)

La escalera de packs se decide contra lo que el cliente puede encontrar en su país. En un caso real, la oferta se iba a fijar en $46.600 por unidad sin saber que Mercado Libre la vendía a $29.500–$49.900.

1. **Mercado Libre del país** (Playwright): `https://listado.mercadolibre.com.<tld>/<terminos-con-guiones>` (`.co`, `.mx`, `.cl`, `.pe`, `.com.ar`…) con el nombre del producto, el nombre del listing y el nombre local. Extrae `li.ui-search-layout__item, div.poly-card` → título, precio (`.andes-money-amount__fraction`), vendedor y si es envío del exterior. Ignora los `click1.mercadolibre…` (son publicidad de otros productos).
2. **Lo que le llega desde el exterior** (lo que el cliente compara de verdad):
   - **Amazon con envío a `<PAIS>`**: busca en amazon.com con la ubicación fijada en el país y anota precio en USD + envío + depósito de importación, y el total en `<MONEDA>`. Si sale "no se envía", anótalo: es una ventaja.
   - **AliExpress, Temu y Shein** con destino al país: precio y días de entrega.
   - **Mercado Libre "envío del exterior"**: suele ser el piso de precio.
3. **Retail local** (grandes superficies, farmacias si es salud o belleza) y **TikTok del país** (mayoristas y tiendas, con `locationCreated:"<CC>"`).
4. **Meta Ad Library del país** (Regla 1b): quién lo pauta y con qué oferta.
5. Escribe en `PRODUCTO.md` una tabla **"Mercado local"**: canal · vendedor · precio por unidad · packs · envío (días, desde dónde) · link. Anota el precio mínimo, el típico y el máximo **puesto en el país** (con envío e impuestos).
6. **Regla de precio:** si el precio por unidad del pack principal queda más de un 30–40 % por encima del típico de Mercado Libre, la landing tiene que justificarlo (experiencia, pago contra entrega, envío gratis, regalo, bundle). Si no, baja el precio o cambia el producto. Dilo en la sección "Oferta" del Artifact.
7. La economía se calcula con el costo que da el usuario. **Nunca propongas un pack sin costo real**; si no lo hay, pregúntalo antes de cerrar la oferta.

## ⭐ REGLA 0e — Landings que venden el producto en EE. UU. y el extranjero (siempre)

Además de los anuncios, **analiza las páginas de producto** de las tiendas extranjeras que venden el mismo formato (Amazon, Shopify DTC, Ulta, Superdrug, TikTok Shop). Son la referencia de landing, no Mercado Libre.
1. Encuéntralas con WebSearch: `"<nombre del listing>" shop`, `<formato> buy`, y con los dominios de los anuncios de Meta ALL.
2. Ábrelas en Playwright a 390 px, toma una captura de página completa y extrae: titular, subtítulo, orden de los bloques, precio y packs, prueba social, garantía, FAQ, uso de GIF o video, y CTA.
3. Escribe `LANDINGS.md`: una ficha por tienda (✅ copiar / ❌ ignorar) y una **estructura recomendada** que mezcle lo mejor de todas. Esa estructura alimenta la sección 6 del Artifact y la skill `landing-cod`.

## ⭐ REGLA 0b — Cazar GEMELOS EXACTOS fuera de Meta (AliExpress → TikTok), siempre

El usuario quiere **replicar creativos ya mismo**, y eso solo sirve con el producto idéntico. Meta muchas veces no tiene gemelos activos; TikTok y AliExpress sí. Hazlo en toda investigación, después de la Regla 0:

1. **AliExpress primero (identificar el SKU white-label):** en el navegador, `https://www.aliexpress.com/w/wholesale-<terminos>.html?SearchText=<terminos en inglés>`. Haz scroll y extrae `a[href*="/item/"]` con su imagen. Arma la hoja de miniaturas y compárala con las fotos del producto. Abre la ficha del candidato y **confirma material, tallas y forma**. Anota en `PRODUCTO.md`: nombre exacto del listing, vendedor, link, precio y la fábrica si aparece. **Ese nombre exacto es la llave para buscar gemelos.**
2. **TikTok (sin login):** `https://www.tiktok.com/search/video?q=<termino>`. Haz scroll lento (`mouse.wheel` 700 px × 8). Extrae `a[href*="/video/"]` + img + likes. Usa el nombre del listing de AliExpress, sus variantes en inglés y los términos del problema en ES/EN/PT. Arma la hoja de miniaturas → verificación visual.
3. **Detalle de cada gemelo:** abre el video y lee `script#__UNIVERSAL_DATA_FOR_REHYDRATION__` → `__DEFAULT_SCOPE__['webapp.video-detail'].itemInfo.itemStruct`: `desc`, `createTime`, `stats.playCount/diggCount/shareCount`, `author.uniqueId`, **`isAd`** (true = anuncio pagado = señal de que vende).
   - **Anuncios de TikTok Shop:** no traen `playAddr` (el video es `blob:`) → márcalos **"probable (TikTok Shop)"** y pide al usuario verificarlos en el celular.
4. **TikTok Creative Center (Top Ads)** como complemento: ver [references/tecnico-busqueda.md](references/tecnico-busqueda.md).
5. **Entrega** en el chat y en `LINKS.md` (sección "GEMELOS EXACTOS"): cuenta, si es orgánico o anuncio, video, reproducciones/likes/compartidos/fecha y link. Más el link del listing de AliExpress. Lista también los descartados por visual.
6. Si tampoco hay gemelos en TikTok, dilo, y recomienda los creativos del proveedor (Drive o AliExpress) como la vía más rápida para replicar.
7. **Descarga SIEMPRE los videos** de gemelos y referencias top a `<producto>/media/ref_<plataforma>_<cuenta>_<tipo>.mp4`. No esperes a que el usuario lo pida. Y **verifica el producto viendo fotogramas del video descargado**: la descripción engaña.
   - **TikTok:** `playAddr` + cookie `tt_chain_token` → curl. **Meta:** `video.src` vía TreeWalker → curl el mismo día (caduca). Comandos en [references/tecnico-busqueda.md](references/tecnico-busqueda.md). Nunca fetch + `<a download>` (cierra el navegador).
   - ⚠️ Deja claro al usuario que los videos de terceros son **referencia**, no para pautar tal cual (derechos de autor y rechazo). Excepción: los de la fábrica o el proveedor.
   - **Material de fábrica para el b-roll:** el video de la galería del listing de AliExpress del SKU exacto suele traer tomas limpias (personas usando el producto, detalles, macro). Ábrelo en Playwright y lee `document.querySelectorAll('video')` → `src` → curl. **Verifica la versión con fotogramas**: en un caso real, 7 de 9 listings "iguales" eran otra versión del producto y uno traía la marca de otra tienda estampada. Si el mismo plano aparece en cuentas de creadores o competidores (con su marca de agua o subtítulos), no es material de fábrica.
   - Documenta cada archivo en `INDEX-CREATIVOS.md` (qué es, si es gemelo o similar, qué tomar).

## ⭐ REGLA 4b — Elegir FORMATOS con el catálogo (siempre, al cerrar la investigación)

**El formato lo elige la investigación, no la costumbre.** Si no, cada producto sale con la misma parrilla del anterior. Procedimiento obligatorio en [references/seleccion-formatos.md](references/seleccion-formatos.md):
0. **Descubrir formatos nuevos (radar en cada ronda):** los 10 anuncios más longevos de la categoría, los 5 TikTok top y 5 anuncios PROBADOS de otras categorías de contraentrega. Lo que no encaje en el catálogo y sea repetible se agrega a `FORMATOS.md` → "🆕 Formatos descubiertos", con referencia y muestra, y se le avisa al usuario (que puede vetarlo).
1. **Etiquetar el formato** de cada referencia en `LINKS.md` (columna Formato) → tabla "Formatos del mercado" con puntos de evidencia.
2. **Puntuar el catálogo** para este producto: evidencia + encaje + nivel de conciencia + material − rotación ± historial de `REGISTRO-FORMATOS.md` (plantilla en `templates/`).
3. **Reglas duras:**
   - ≥ 50 % de los formatos con una referencia real de la investigación;
   - máximo 4 repetidos del producto anterior;
   - un formato por ángulo;
   - ≥ 3 familias por ángulo;
   - el formato más fuerte del mercado va siempre;
   - 1 comodín nuevo por ronda.
4. **`MATRIZ.md` con la columna "Por qué este formato"** (referencia y puntos) y la lista de descartados. Se le muestra al usuario antes de producir.
5. **Registrar** en `REGISTRO-FORMATOS.md` al publicar, y completar el resultado en la lectura.

Lee [references/formatos.md](references/formatos.md) (la copia de trabajo, que el usuario va ampliando, vive en `<carpeta de trabajo>/FORMATOS.md`). El plan de testeo del Artifact sale como **matriz ángulo × formato**:
- Cada anuncio lleva un solo ángulo, y cada ángulo va en varios formatos. Mínimo 3 ángulos × 4 formatos: video con voz, video sin voz, estático nativo y estático de argumento.
- Siempre al menos una pieza TOFU, que no se apaga aunque venda caro.
- Por cada celda: ángulo, formato, etapa, gancho y el material con el que se produce.

Cada guion sigue la estructura **gancho (0–3 s, en 3 capas: imagen, texto y voz) → cuerpo (agitar, mecanismo, prueba, objeción) → CTA (oferta real, riesgo cero, instrucción y tarjeta)**. Los anuncios se nombran `PRODUCTO_ANGULO_FORMATO_GANCHO_v`.

La primera prueba sigue la **metodología RECON**:
- 4 ángulos base (dolor, identidad, oportunidad y autoridad) × ganchos, con la misma audiencia.
- De 5 a 7 días, con gasto parejo (entrega push o ABO).
- Al ganador se lo pasa a la campaña principal.

Los formatos de video con IA se producen con Magnific Spaces si está conectado ([references/video-ia-spaces.md](references/video-ia-spaces.md)); si no, se marcan "⏳ pendiente". Las reseñas, la escasez y las estadísticas salen de datos reales del producto o de la operación, nunca inventados.

**⭐ Todo anuncio explica el producto (aprendido el 2026-10-23).** El formato decora, no reemplaza la explicación. En una RECON de un producto nuevo para el mercado, el usuario rechazó como "0 explicativos" el texto sobre negro, el titular de noticia, la pantalla dividida, la historia de IG, el precio por día, el tipo TikTok y el unboxing armados sin mostrar qué hace el producto. Solo se salvaron la demostración en video y 3 estáticos con el producto visible. Por eso cada pieza, sea del formato que sea, lleva:
- el **producto visible y reconocible**;
- **una línea de mecanismo** (qué hace y cómo: "6 bolsas de aire que aprietan + calor en la frente");
- el **beneficio**.

En video, la demostración del uso va en los **primeros 3–5 s**, no al final. Antes de mostrar al usuario, haz la **prueba de los 2 segundos**: tapa el logo y pregúntate "¿se entiende qué vende y qué hace?". Si no, rehazlo. Cuanto menos conozca el mercado el producto (nadie lo vende en el país), más pesa esta regla.

## ⭐ REGLA 5 — Si el usuario pide videos o imágenes propias para testear

**Material permitido (no negociable):** fotos y videos del proveedor o la fábrica + escenas generadas con Codex + **stock licenciado** (el que diga `CONFIG-TIENDA.md`, p. ej. Magnific/Freepik; solo para escenas de contexto, nunca donde la voz nombra el producto) + material grabado por el usuario. **Nunca** pautar ni usar como b-roll videos de competidores o creadores, aunque el usuario lo pida: son referencia de estructura. Alternativas: videos del proveedor con el guion de la referencia, grabar una unidad, o licenciar al creador.

Pipeline probado: guion por referencia → **avatar con voz propia en VoxCPM2** (voz base diseñada por descripción + actuación frase por frase) → validación y tiempos por palabra con whisper → música propia (`scripts/gen_music.py`) → subtítulos PNG → b-roll de fábrica + stock + imágenes Codex → función `build` de ffmpeg → QA con fotogramas → **mostrar al usuario** → Shopify Files → Meta por API. Detalle:
- Guion, voz, música, material, stock y QA: [references/produccion-creativos.md](references/produccion-creativos.md).
- **Voces por avatar (motor recomendado):** cada guion tiene un avatar (edad, región, personalidad) y el avatar tiene su propia voz con acento acorde; guion en estilo UGC de corrido y actuación dirigida frase por frase: [references/voces-voxcpm2.md](references/voces-voxcpm2.md).
- Respaldo con OmniVoice (instalación, API, errores conocidos): [references/voces-omnivoice.md](references/voces-omnivoice.md).
- Montaje con ffmpeg (función lista para copiar) y subida a Meta paso a paso: [references/montaje-ffmpeg.md](references/montaje-ffmpeg.md). Incluye los estáticos 4:5 + 9:16 en un solo anuncio y la RECON con presupuesto por conjunto (ojo con las monedas sin centavos).
- Clips de uso con IA cuando el material del proveedor no muestra el producto en uso: Claude arma el Space de Magnific (imagen inicial fiel + prompt + modelo) y **el usuario genera** con sus modelos ilimitados: [references/video-ia-spaces.md](references/video-ia-spaces.md).

La **landing** del producto (packshot, 7 piezas, GIFs, Shopify, packs) es otra skill: `landing-cod`.

## ⭐ REGLA 1 — SIEMPRE entregar los links (no negociable)

**Toda ronda termina con links clicables en el chat, no solo en archivo.** Nunca entregues solo nombres de marca, ganchos o análisis: sin link no sirve.

Se entregan **tres cosas, siempre**:

1. **Anuncio individual** → `https://www.facebook.com/ads/library/?id=<ad_id>`
   ⚠️ Meta ya NO aísla un anuncio con `?id=` solo: reescribe la URL a la biblioteca de la página. Para abrir un anuncio concreto, usa el link filtrado por frase (ver más abajo).
2. **Biblioteca completa del anunciante**:
   `https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&is_targeted_country=false&media_type=all&search_type=page&view_all_page_id=<page_id>`
   ⚠️ `view_all_page_id` funciona para páginas de MARCA/tienda, pero NO para páginas de PERSONA/advertorial. Para esas, usa el link filtrado por frase.
3. **Los videos descargados por ti.** Bájalos en la misma ronda, sin que el usuario exporte nada: Meta con el `video.src` de la Ad Library y TikTok con `playAddr` (ver "Descarga de creativos" y [references/tecnico-busqueda.md](references/tecnico-busqueda.md)). El swipe de la extensión solo se ofrece si hay que bajar una biblioteca entera de decenas de anuncios.

**Link filtrado por frase (abre un anuncio o grupo concreto):**
`https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=<CC|ALL>&is_targeted_country=false&media_type=<all|video|image>&search_type=keyword_unordered&q=<frase única del anuncio, sin tildes>`
El buscador de Meta ignora tildes. Una frase única del copy suele reducir de miles a 1–5 resultados.

Formato de entrega en el chat: agrupa por anunciante o por bloque (propios / directos / similares-por-ingrediente / referencia internacional), y para cada anuncio da **gancho + señal de longevidad + link individual**, y la ruta del video descargado. Si la lista pasa de ~25 links, además publica un Artifact con todo clicable y deja en el chat solo el top.

**Etiqueta siempre el nivel de evidencia:**
- `PROBADO` — relanzado tras pausa, o +90 días entregando continuo.
- `INDICIO` — biblioteca grande o muchos ángulos, pero pocos días de vida.
- `SIN PROBAR` — lanzamiento reciente; se reporta para vigilar, no para copiar.

Nunca presentes un `INDICIO` como si fuera `PROBADO`.

## ⭐ REGLA 2 — NO repetir lo ya entregado

**Antes de cualquier búsqueda, lee `<CARPETA>/REGISTRO-INVESTIGACION.md`** y la sección `## 🔗 ANUNCIOS YA ENTREGADOS` del producto correspondiente.

El control es **a nivel de anuncio individual (`ad_id`)**, no solo de anunciante. Un mismo competidor puede volver a aparecer con creativos nuevos: eso sí se reporta. Lo que nunca se repite es un `ad_id` ya entregado.

En cada ronda:
1. Omite todo `ad_id` que ya esté en el registro.
2. Si un anunciante ya está cubierto pero tiene creativos nuevos, repórtalos marcando "ya en registro, creativos nuevos".
3. Si una búsqueda entera solo devuelve material ya entregado, **dilo explícitamente** en vez de rellenar repitiendo.
4. Al terminar, **actualiza el registro** con: `ad_id`s entregados, page_ids, términos usados y pendientes.

### Formato obligatorio del registro de anuncios entregados

```markdown
## 🔗 ANUNCIOS YA ENTREGADOS — <producto> (NO volver a reportar estos ad_id)

| ad_id | Anunciante | page_id | Gancho | Evidencia | Ronda |
|-------|-----------|---------|--------|-----------|-------|
| 2185579072255550 | EjemploCompetidor | 677045318828393 | COMIENZA HOY A CUIDAR TUS ARTICULACIONES | PROBADO 87d | R1 |
```

```markdown
### Bibliotecas (view_all_page_id) ya entregadas
- 677045318828393 EjemploCompetidor · 971140376079650 EjemploGlobalUS · ...
```

## ⭐ REGLA 0c — Si el producto YA está pautado, empieza por los datos propios

Antes de buscar fuera:
1. Saca de Meta la campaña activa: copy y título de cada creativo (`ads_get_creatives` con `creative_ids`), CPA por anuncio, y los cortes **edad×género** y **plataforma×ubicación** con `date_preset=maximum`. Eso define el avatar real (ej.: un producto de regalo compraba 35+ y la franja 25–34 era la peor).
2. Saca de Shopify precio, compare_at y descripción (`graphql_query` con `title:*X*`). Si hay un **compare_at ficticio**, márcalo como riesgo legal (precio de referencia engañoso) en `PRODUCTO.md`.
3. Si la tienda usa el plugin **cod-ops**, saca la economía real de su `data.json` (ingreso, despacho, entrega, utilidad por familia) para el break-even y el target CPA.
4. Lista qué **no** dicen los anuncios actuales: ahí suelen estar los ángulos nuevos.

**Producto nuevo (sin historial):** estima el break-even por pedido con
`tasa_despacho × [tasa_entrega × (precio − costo − flete) − (1 − tasa_entrega) × (flete + flete_devolución)]`
(por defecto 80 % despacho y 90 % entrega; usa las tasas de `CONFIG-TIENDA.md`). Ejemplo: pack ×2 a $89.900, costo $24.000, flete $15.500 ≈ $33.800. Target CPA ≈ 55–60 % del break-even. Si la tienda usa cod-ops, la familia nueva se da de alta con `/cod-ops:setup-tienda`.

## Lecciones de campo (rondas reales)
- **El nombre en inglés del listing de AliExpress destapa las redes globales:** un término local solo devolvía 1 anunciante; el nombre del listing en inglés devolvió ~460 anuncios del mismo SKU. Busca siempre en el idioma local **y** con el nombre del listing en inglés.
- **"N anuncios usan este contenido"** en la Ad Library = la red de dropshippers reusa ese corte. Muchas tiendas con el mismo copy + mismo video = INDICIO masivo (no PROBADO si todos tienen <60 días).
- **Edad real del creativo** (`efg=` → `asset_age_days`), **notificaciones de TikTok** colándose en la búsqueda con sesión, **ruido de `ads_library_search`** con términos genéricos y **hojas de miniaturas sin Pillow**: ver [references/tecnico-busqueda.md](references/tecnico-busqueda.md).
- **Nombres ya tomados** → ver Regla 0, paso 2b.
- **Patrones de producto de regalo/coleccionable:** ASMR de armado (bandeja → herramienta → terminado), "mi nueva terapia" (desconexión), nostalgia ("la bici de mi papá"), Navidad "regalo para el que tiene todo", colección por colores. La red global arranca la temporada navideña en **agosto–septiembre**.
- **Hooks que bloquean escritura** (si el usuario tiene un plugin tipo SDD): usa `>/dev/null` para salidas; los `.md` con Write/Edit; curl/ffmpeg/codex escribiendo media suelen pasar. Detalle: [references/entrega-artifact.md](references/entrega-artifact.md).

## Fuentes de datos (en orden de preferencia)

1. **Meta Ad Library API** — tool `ads_library_search` (MCP de Meta Ads). Vía principal, sin navegador.
   - Buscar por `search_terms` o por `page_ids`.
   - Flujo típico: `search_terms` con el nombre de marca → `page_id` del primer resultado → re-consulta con `page_ids` para traer toda su biblioteca.
   - `estimated_total_count` = volumen de anuncios de esa marca (señal de inversión / escala).
   - **Limitación:** la API NO devuelve el archivo de video/imagen, solo `ad_snapshot_url`.
   - El campo `ad_creative_link_title` suele revelar el ÁNGULO. Es oro para el banco de ángulos.
   - Ojo con nombres de marca ambiguos: filtra por `page_name`/`page_id` real.

1b. **Ad Library en el navegador (Playwright, `browser_run_code_unsafe`)**: trae el **copy completo, la fecha "En circulación desde" y el orden por impresiones**. La API ordena por fecha de creación y entierra a los longevos.
   - Varias búsquedas por llamada, parseo de `innerText` y verificación visual con TreeWalker + hoja de miniaturas: ver [references/tecnico-busqueda.md](references/tecnico-busqueda.md).
   - Las búsquedas por frase larga a veces devuelven otro anuncio; verifica que el `id` coincida.
   - WebFetch a `facebook.com/ads/library` falla; usa siempre el navegador.

2. **WebFetch a las landing pages** — las landings repiten el copy (titular, beneficios, oferta, garantía). Si un dominio bloquea con 403, usa el navegador.

3. **Descarga de creativos (sin swipe).** Tú los descargas en la misma ronda:
   - **Meta:** en Playwright abre la búsqueda por frase o término (país y ALL), haz scroll y recorre el DOM con TreeWalker: cada texto `biblioteca: <id>` abre un anuncio y el primer `VIDEO` con `src` que aparece después es su video. Baja cada uno con `curl -A "Mozilla/5.0" -o <producto>/media/ref_meta_<anunciante>_<angulo>.mp4 "<src>"` **el mismo día** (caducan en horas). El parámetro `efg` (base64) trae `asset_age_days` y `duration_s`: anótalos.
   - **TikTok:** `playAddr` de la rehidratación + cookie `tt_chain_token` → curl.
   - Las URL son largas: pásalas a curl con un heredoc `while read archivo url`, sin reescribirlas a mano.
   - **Verifica cada gemelo con fotogramas al 20, 50 y 80 %** antes de llamarlo gemelo.
   - Ficha de cada archivo en `INDEX-CREATIVOS.md`. Después, fotogramas con `ffmpeg` para leer los subtítulos quemados y reconstruir el guion.
   - Opción para bibliotecas enteras: la extensión `extension/` exporta `swipe_file.json` y `scripts/download_swipe_media.py` lo descarga.

## Cómo decidir qué es "competidor compatible"

Define el producto primero. **Extrae y anota sus INGREDIENTES/ACTIVOS y su MECANISMO**. Esos son la llave para encontrar productos similares. Luego clasifica:

- **Gemelo (white-label):** el MISMO producto físico que revende otra marca. Suelen reciclar un kit de creativos compartido. Es la mina para copiar/traducir directo.
- **Directo:** mismo producto/categoría y mismo público, otra marca.
- **Similar por ingrediente/mecanismo:** distinto producto pero con **el mismo activo o mecanismo**. Aquí está el oro para **VARIACIONES**.
- **Adyacente:** mismo público pero distinto ángulo.
- **Excluir:** otra categoría y **falsos positivos por keyword**.

Ordena de mejor a peor con: **longevidad (días activo) + cercanía al producto + mercado/idioma + tiene copy real**. Lo que lleva +300 días corriendo casi siempre es rentable.

## ⭐ REGLA 3 — SIEMPRE buscar productos similares por ingrediente (para variaciones)

1. Del producto, lista sus **activos principales** y su **mecanismo/beneficio central**.
2. Busca en la Ad Library por cada activo y por el mecanismo, no solo por marca, y en varios idiomas/mercados.
3. Detecta **gemelos white-label**: el mismo copy en muchos anunciantes = mismo producto reempacado → prioriza.
4. De los similares, extrae **gancho, ángulo, formato, oferta**, anotando el origen.
5. Vuélcalos al `BANCO-ANGULOS.md` en **"Variaciones desde productos similares"**.

Regla de claims al variar: nunca copies claims prohibidos (curar, regenerar, reemplazar medicación). Reencuadra al claim defendible del activo.

## ⭐ REGLA 4 — Entregable final: INVESTIGACIÓN CREATIVA COMPLETA (siempre)

Toda investigación termina en **un solo Artifact publicado** que reúne todo el producto (todas las rondas), listo para construir la landing y los anuncios. Mismo archivo y misma URL en cada ronda. Su link va en `INICIO.md` y al inicio de `LINKS.md`.

Son **21 secciones en orden fijo**: primero lo de la landing (A: resumen, avatares, dolores, conciencia, ángulos, gemelos, estructura de landing, titulares, oferta sin "antes" ficticio, claims, FAQ, mapa de media, referencias, coherencia) y después la investigación (B: ranking, análisis, copy, testeo, economía, anuncios entregados, bibliotecas, pendientes). Lista completa: [references/entrega-artifact.md](references/entrega-artifact.md).

## Entregables (usa las plantillas de `templates/`)

- **PRODUCTO.md** — ⭐ SIEMPRE (Regla 0).
- **INVESTIGACIÓN CREATIVA COMPLETA (Artifact)** — ⭐ SIEMPRE (Regla 4).
- **LINKS.md** — ⭐ SIEMPRE. Lista maestra de anuncios entregados por bloque, con gancho, evidencia y link; más la tabla de bibliotecas.
- **RANKING.md**, **COPY.md**, **ANALISIS-BIBLIOTECAS.md**, **INDEX-CREATIVOS.md**.
- **BANCO-ANGULOS.md** — ⭐ el más accionable: ~12 ángulos × ofertas × formatos + plan de testeo de 3 rondas + "Variaciones desde productos similares".

## Patrones ganadores recurrentes

- **Vender la OFERTA y la LOGÍSTICA, no el feature**: "pago contra entrega", "envío gratis", "-30% 2ª unidad", 2×1. En mercados con desconfianza al pago online (gran parte de LATAM), contra entrega es la palanca #1.
- **Dato + plazo en el titular**: "resultados en 14 días".
- **Numerología en el titular**: `Nº ingredientes + Nº tomas + Nº días`.
- **Banco de muchos ángulos sobre un mismo producto**: dato, edad/miedo, dolor específico, objeción, "el único con…", prueba social.
- **Autoridad con rostro y nombre**.
- **Embudo advertorial**: página de "persona" → listicle → producto.
- **Escalera de packs + bonus de regalo** (el del medio marcado como ahorro).
- **LTV / marca**: el cliente de una categoría recompra.

## Flujo de una ronda de investigación

0. Leer `CONFIG-TIENDA.md` (si no existe → `setup-creativos`).
1. Leer `REGISTRO-INVESTIGACION.md`, **incluida la tabla `🔗 ANUNCIOS YA ENTREGADOS`**.
2. **(Regla 0) Verificar el producto REAL** y escribir o actualizar `PRODUCTO.md`.
2b. **(Regla 0b) Gemelos exactos fuera de Meta**: AliExpress → TikTok, con verificación visual.
2c. **(Regla 0d) Mercado local** → tabla de precios en `PRODUCTO.md`. Pedir el costo real antes de proponer packs.
2d. **(Regla 0e) Landings extranjeras** → `LANDINGS.md`.
3. Buscar competidores NUEVOS con `ads_library_search` (marcas, términos en inglés y en el idioma del país). Sacar page_ids y volúmenes.
3a. **(Regla 4b, Paso 0) Radar de formatos:** 5 anuncios PROBADOS de otras categorías de contraentrega (hogar, belleza, mascotas, juguetes), buscados por "pago contra entrega" y ordenados por días activos. Solo interesa su **formato**.
3b. **(Regla 3) Similares por ingrediente/mecanismo.**
4. **Filtrar contra el registro.**
5. Clasificar y rankear. Asignar PROBADO / INDICIO / SIN PROBAR **y el FORMATO** de cada referencia (nombre del catálogo o `🆕`).
6. Extraer copy de los mejores (WebFetch).
7. **Descargar tú mismo los videos**, verificarlos con fotogramas y fichar cada uno en `INDEX-CREATIVOS.md`.
8. **Entregar los links en el chat** (Regla 1).
9. Generar/actualizar los entregables, **siempre incluido `LINKS.md`**.
10. **Actualizar `REGISTRO-INVESTIGACION.md`.**
11. **(Regla 4) Publicar o actualizar la INVESTIGACIÓN CREATIVA COMPLETA.**

> ⚠️ Una ronda NO está terminada si: no hay tabla de mercado local (0d), no se analizaron landings extranjeras (0e), el producto no está verificado (0), el usuario no recibió links clicables, el registro no tiene los `ad_id`, la investigación creativa completa (4) no está publicada, **la matriz no tiene "Formatos del mercado" y la columna "Por qué este formato", repite más de 4 formatos del producto anterior, o no se corrió el radar de formatos ni se le reportaron al usuario los nuevos (aunque sean cero) (4b)**.

## Reglas de costo y estilo

- "Documentar primero": API + WebFetch + scripts. Para la Ad Library, el navegador con varias búsquedas por llamada.
- No vuelques miles de anuncios crudos en el chat; sintetiza y guarda en archivo.
- Responde en el idioma del usuario (código y nombres de archivo en inglés).
- Cambia 1 variable por ronda de test (ángulo → oferta → formato).
- **Nada se publica en Meta ni se activa en Shopify sin el visto bueno explícito del usuario.**
