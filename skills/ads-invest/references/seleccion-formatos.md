# Selección de formatos: de la investigación a la matriz

> **Por qué existe:** sin este procedimiento, cada producto termina con la misma parrilla de formatos del producto anterior (por ejemplo: Dolor = nota del iPhone, Google, tachados y notificación; Identidad = WhatsApp, historia y ticket…), aunque la investigación muestre otros ganadores (primera vez, reverso, unboxing probado, carta de disculpa).
> **Regla de oro:** el formato lo elige la investigación, no la costumbre. Cada formato de la matriz tiene que poder decir "lo elegí por este anuncio o por este dato".

Archivos de trabajo (en la carpeta de trabajo del usuario):
- `FORMATOS.md`: copia de trabajo de [formatos.md](formatos.md), que el usuario va ampliando.
- `REGISTRO-FORMATOS.md`: qué formato se usó en cada producto y cómo le fue. Plantilla en `templates/REGISTRO-FORMATOS.md`.
- `formatos/descubiertos/`: muestras de los formatos nuevos.

## Paso 0 — Descubrir formatos nuevos (en cada investigación)
El catálogo no está cerrado: la investigación también tiene que **encontrar formatos que todavía no tenemos** y agregarlos.

**Radar de formatos (búsqueda activa, cada ronda):**
1. **En la categoría:** los 10 anuncios más longevos (PROBADO) y los 5 TikTok con más vistas del producto y de sus similares.
2. **Fuera de la categoría:** 5 anuncios PROBADOS de otras categorías de contraentrega del mismo país y nivel de precio (hogar, belleza, mascotas, juguetes). Se buscan en la Ad Library por frases como "pago contra entrega" o "envío gratis" y se ordenan por días activos. Los formatos que ya funcionan en otro nicho son los que la competencia del nuestro todavía no usa.
3. **Fuentes del usuario:** si mandó reels o listas de formatos de especialistas, se procesan igual (fotogramas + transcripción) y se agregan.

**Cuándo algo es un formato nuevo (y no solo un gancho distinto):** tiene que cumplir las 3 condiciones:
- **Estructura repetible:** se puede describir como una plantilla (cómo se ve, qué se dice y en qué orden) y aplicar a otro producto.
- **Distinto:** no encaja en ninguna fila del catálogo, y tampoco como variante menor de una.
- **Visto funcionando:** al menos una referencia con 1 punto de evidencia (Paso 1). Un anuncio PROBADO o un TikTok con más de 1 M de vistas lo vuelve prioritario.

**Qué se hace con cada formato nuevo:**
1. Se agrega a `FORMATOS.md`, sección **"🆕 Formatos descubiertos"**, con: nombre corto, qué es (1 línea), etapa del embudo, cómo lo producimos con nuestras herramientas (voz, fábrica, Codex, HTML, stock) y sus ⚠️, referencia (ad_id o cuenta, con link), evidencia, producto y fecha del hallazgo.
2. También entra a la tabla "Formatos del mercado" del producto. Si tiene ≥ 2 puntos, **es candidato al comodín** de la ronda (regla 6 del Paso 3).
3. Se guarda una muestra (video o captura) en `formatos/descubiertos/<nombre>_<ref>.<ext>`.
4. **Se le avisa al usuario en el chat** con la lista de formatos nuevos y su referencia. El usuario puede vetar alguno (pasa a "Descartados", con la razón) o aprobarlo. Si el radar no encontró nada nuevo, también se dice.
5. **Estado:** 🆕 descubierto → 🧪 en prueba (publicado en una prueba) → ✅ validado (ganó en `REGISTRO-FORMATOS.md`) o ❌ no funcionó (con el producto). Al validarse, pasa a su sección del catálogo.

## Paso 1 — Etiquetar el formato de cada referencia (durante la investigación)
En `LINKS.md`, cada anuncio de Meta y cada video de TikTok lleva una columna **Formato** con el nombre exacto del catálogo, además del gancho y la evidencia. Si un anuncio no encaja en ningún formato del catálogo, se etiqueta como `🆕 <nombre propuesto>` y se procesa con el Paso 0.

Al cerrar la investigación, se resume en una tabla **"Formatos del mercado"** (en `MATRIZ.md` y en el entregable final):

| Formato | Referencias (ad_id / cuenta) | Mejor evidencia | Puntos |
|---|---|---|---|
| Primera vez / reacción | TikTok MX (anuncio) | 30,4 M vistas | 3 |
| Unboxing | Meta, anunciante de contraentrega | PROBADO, 2 años | 3 |

**Puntos de evidencia:**
- **3:** PROBADO en Meta (≥ 90 días o relanzado), o anuncio de TikTok con más de 1 M de vistas.
- **2:** INDICIO (30–89 días o varias variantes), o entre 100 K y 1 M de vistas.
- **1:** SIN PROBAR, o un orgánico.

Si el mismo formato aparece en varias referencias, se suma, con tope de 6.

## Paso 2 — Puntuar el catálogo para ESTE producto
Por cada formato candidato (todos los del mercado, más los del catálogo que encajen):

| Criterio | Puntos |
|---|---|
| Evidencia del Paso 1 | 0–6 |
| Encaje con el producto: se demuestra visualmente, tiene un mecanismo que se explica, es regalable, es para la familia o pide comparación | 0–2 |
| Encaje con el **nivel de conciencia** del avatar: no sabe que tiene el problema → educativo, titular de noticia o Google · conoce el problema → problema-solución, testimonio o demostración · conoce las soluciones → vs., mito o tier list · conoce el producto → oferta, ticket o disculpa | 0–2 |
| Hay material real para producirlo (fábrica, Codex con fotos reales, stock, voz) | 0 a −3 (se descarta si pide algo prohibido) |
| **Rotación:** se usó en el producto anterior (`REGISTRO-FORMATOS.md`) | −2 |
| **Historial:** en `REGISTRO-FORMATOS.md`, ganó (CPA bajo el objetivo) / perdió (sin ventas con más de 1× el CPA objetivo gastado) | +2 / −2 |

## Paso 3 — Armar la matriz con reglas duras
1. **Al menos el 50 % de los formatos sale del Paso 1**, con una referencia real (ad_id o cuenta). El resto puede venir del catálogo, justificando el encaje.
2. **Máximo 4 formatos repetidos** de la matriz del producto anterior. Se verifica contra `REGISTRO-FORMATOS.md` antes de producir.
3. **Un formato, un solo ángulo** dentro de la misma ronda: no se repite "nota del iPhone" en Dolor y en Identidad. Excepción, justificada por escrito: el formato con más puntos puede ir en 2 ángulos para compararlos.
4. **Cada ángulo cubre al menos 3 familias:** 🎙️ video con voz · 🎬 video sin voz · 🖼️ estático nativo · 🖼️ estático de argumento · 💰 oferta/BOFU.
5. **El formato más fuerte del mercado va siempre**, aunque cueste producirlo. Si no se puede producir (por ejemplo, avatar de IA), se hace su versión posible y se marca "⏳ versión completa pendiente".
6. **Un formato comodín por ronda:** nunca probado en la cuenta y con al menos 1 punto de evidencia (para descubrir).
7. **Embudo:** al menos 1 TOFU por ángulo, que no se apaga aunque venda caro.
8. Los ángulos se mantienen (RECON con los 4 base: dolor, identidad, oportunidad y autoridad). Lo que rota es el formato.

## Paso 4 — Escribirlo en la matriz (con el porqué)
`MATRIZ.md` lleva, por anuncio, las columnas **ID · Ángulo · Formato · Familia · Etapa · Gancho · Por qué este formato (referencia + puntos) · Material**. Debajo va la lista **"Formatos descartados"** con el formato y la razón (sin material, prohibido, poca evidencia o repetido).

Antes de producir, se le muestra al usuario la tabla "Formatos del mercado" junto con la matriz, para que vea que la elección sale de la investigación.

## Paso 5 — Registrar y cerrar el ciclo
- Al publicar, se agrega una fila por formato en `REGISTRO-FORMATOS.md`: producto, fecha, ángulo, formato y ad_id.
- En la lectura (5–7 días) se completan gasto, compras, CPA y veredicto (✅ ganó · ➖ neutro · ❌ perdió). Ese historial alimenta los puntos del Paso 2 en el próximo producto.

## Ejemplo: irrigador bucal (investigación real, referencias públicas)
| Ángulo | Formatos elegidos (y por qué) |
|---|---|
| Dolor | 🎙️ **Primera vez usándolo** (30 M) · 🖼️ **Titular de curiosidad** (anuncio de curiosidad de la categoría) · 🖼️ Google (el avatar busca el síntoma) |
| Identidad | 🎙️ **UGC brackets** (dos anuncios UGC de la categoría) · 🖼️ Chat de WhatsApp entre mamás · 💰 **Pack ×2 "para la familia"** (el más vendido en Amazon) |
| Oportunidad | 🎙️ **Reverso "me da pena con los que compraron esto…"** (17 M) · 🖼️ Efecto secundario · 🖼️ Pantalla dividida |
| Autoridad | 🎙️ **Tutorial de las boquillas** (5,8 M) · 🎬 **Unboxing contraentrega** (PROBADO, 2 años) · 🎬 Macro de demostración · 💰 **Carta de disculpa por un lote real** (PROBADO) · 🖼️ Mito vs. realidad |

Comodín: titular de noticia con la curiosidad. Repetidos del producto anterior: Google, WhatsApp, efecto secundario y mito (4, el máximo).
