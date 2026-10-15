# Catálogo de formatos de anuncio

> Fuente: reels y posts de especialistas en Meta Ads (cuentas en la tabla de referencias). El usuario agrega formatos nuevos: cada formato nuevo es una fila más. La copia de trabajo vive en `<carpeta de trabajo>/FORMATOS.md`.
> Se usa al cerrar cada investigación de `ads-invest`: el plan de testeo dice qué formatos usar por ángulo y por qué.

## La regla madre: ángulo × formato (@burgielias, DY4oyi2Oq6h)
1. Sacar los **ángulos** del producto: dolores, deseos y beneficios del cliente. Cada ángulo es una razón concreta de compra.
2. **Un anuncio = un solo ángulo.** El mismo ángulo se dice en varios formatos (por ejemplo: UGC → testimonio → comparativa → urgencia).
3. Se deja correr una semana, se escala lo que funciona, se pausa lo que no y se suben ángulos nuevos cada semana. Eso es la diversidad creativa. Encaja con One CBO: 15 creativos por semana.

Matriz mínima por producto: **3 ángulos × 4 formatos** (un video con voz, un video sin voz, un estático nativo y un estático de argumento).

## Metodología RECON (validación antes de escalar)
Es un sistema para probar creativos con datos en vez de intuición.
1. **Estructura controlada:** se prueban a la vez variantes de **gancho × ángulo** con la misma audiencia. Lo único que cambia es el creativo.
2. **Los 4 ángulos base** (motivaciones universales), adaptados a e-commerce COD:
   - **Dolor:** el problema. Ej. (plantilla ortopédica): "me dolía la cadera".
   - **Identidad:** quién es el cliente. Ej. (plantilla ortopédica): "mamá que cuida la pisada de su hijo".
   - **Oportunidad:** lo que puede lograr. Ej. (plantilla ortopédica): "terminar el día de pie sin dolor".
   - **Autoridad:** credibilidad. Material, demostración, cifras del producto, experto, reseñas reales.
3. **Medición:** de 5 a 7 días. Se escala la combinación ángulo + gancho con mejor costo por resultado y se itera sobre ella (mismo ángulo en más formatos; ver la regla madre de abajo).

**Cómo lo montamos nosotros:**
- **Matriz base:** 4 ángulos × 2 ganchos = 8 anuncios, cada uno en su conjunto OPEN.
- **Reparto del gasto:** con CBO, Meta concentra el gasto en 1 o 2 anuncios y el resto no recibe datos. Para que la prueba sea pareja, se usa **entrega push** en cada anuncio nuevo o se corre la fase RECON en **ABO** con el mismo presupuesto por conjunto. Al ganador se lo pasa a la One CBO.
- **Presupuesto mínimo:** para leer CPA hacen falta unas 2–3 compras por celda. Con un CPA objetivo de ~$30.000, eso son ~$60.000–90.000 por celda en la semana. Si no alcanza, se reduce a 4 celdas (4 ángulos × 1 gancho) y los ganchos se prueban después.
- **Gancho:** se cambian solo los primeros 3 s (texto, toma y primera frase) y se reusa el cuerpo del video. Es barato de producir: una voz por gancho y el mismo montaje.

## Etapa del embudo (@jhonhmastery, DdeaRYfFC4v)
- **TOFU (descubrimiento):** piezas educativas que hablan del problema desde otro ángulo y hacen que el cliente caiga en cuenta de que lo tiene. Venden "caro" (CPA alto), **pero no se apagan**: sin ellas el resto deja de funcionar.
- **MOFU (consideración):** comparativas, demostración y objeciones.
- **BOFU (cierre):** oferta, reseñas, urgencia real y remarketing (las conversiones más baratas de la cuenta).

## A. Video con voz
| Formato | Qué es | Etapa | Cómo lo producimos |
|---|---|---|---|
| **Testimonio / UGC** | "Me pasaba X, probé esto" en primera persona, casual, no parece anuncio | TOFU-MOFU | Voz OmniVoice D/F + stock + fábrica |
| **Demostración** | El producto haciendo lo que promete | MOFU | Voz + clips de fábrica |
| **Problema → solución** | El dolor en 3 s y luego el producto | TOFU | Voz + stock del dolor + fábrica |
| **Educativo TOFU** | Explica el problema desde otro ángulo, sin vender al inicio | TOFU | Voz + stock + texto; el producto entra al final |
| **"Te voy a contar la verdad"** | Confesión o desmentido ("lo que nadie te dice de las plantillas de gel") | TOFU | Voz + texto grande |
| **Podcast / dualcast IA** | Dos voces conversando sobre el problema | TOFU | Dos voces OmniVoice; imagen fija o b-roll ⚠️ sin avatar de video |
| **Objeto parlante** | El producto habla en primera persona | MOFU | Voz + clips de fábrica; ⚠️ sin animación generada |
| **Antes / después** | Mostrar la transformación, no explicarla | MOFU | Solo con material real; ⚠️ nada inventado ni de salud sin fuente |

## B. Video sin voz
| Formato | Qué es | Etapa | Cómo lo producimos |
|---|---|---|---|
| **Macro con textos** | Producto de cerca con 3 textos y tarjeta | MOFU-BOFU | Fábrica + música |
| **ASMR** | Sonido y manos usando el producto, nativo y educa | TOFU-MOFU | Clips de fábrica con su sonido (si lo tienen) |
| **Tipo TikTok** | Ritmo rápido, texto nativo de TikTok, parece orgánico | TOFU | Fábrica + stock, cortes de 1 s |

## C. Estáticos nativos ("ugly ads", no parecen anuncio)
Se arman en HTML con Playwright, igual que la portada: texto exacto y sin errores. Son los más baratos de producir: muchos en una tarde.
| Formato | Ejemplo |
|---|---|
| **Notas del iPhone** | "Cosas que me cambiaron el día: ☐ mis plantillas nuevas…" |
| **Chat de WhatsApp** | Conversación entre amigas recomendando el producto |
| **Historia de Instagram** | Tipografía de IG sobre una foto casera |
| **Notificación / llamada perdida** | "Llamada perdida: tus pies 🦶" |
| **Búsqueda de Google** | El buscador con la pregunta del dolor |
| **Ticket de compra** | Recibo con el pack y el total (precio real) |
| **Captura de email** | Correo "tu pedido va en camino" |
| **Paint / ugly ad** | Foto de celular con texto mal puesto encima |
| **Titular de noticia** | Abre con novedad o curiosidad, no con "compra" |
| **Estilo Reddit / X** | Pregunta y respuestas de usuarios |

## D. Estáticos de argumento
| Formato | Etapa | Nota |
|---|---|---|
| **Punteo de beneficios** (bullets) | TOFU | "El más subestimado": se lee en 2 s |
| **Nosotros vs. ellos / comparativa** | MOFU | Contra "la plantilla de gel", nunca contra una marca |
| **Lo que tenés vs. lo que podés tener** (viejo vs. nuevo) | MOFU | Foto lado a lado |
| **Problemas tachados** | TOFU | Lista de dolores tachados |
| **X razones por las que…** / **X señales de que…** | TOFU | ⚠️ "señales" de salud solo con fuente |
| **Advertencia / atención** | TOFU | ⚠️ sin miedo médico inventado |
| **Mito vs. realidad** | MOFU | Buen formato para objeciones |
| **Tier list / diagrama / Venn** | MOFU | |
| **Estadística como titular** | MOFU | Cifras sacadas de los datos del producto: specs del proveedor, pedidos, entregas, tallas, materiales |
| **Precio por día** ("menos que un café") | BOFU | precio del pack ÷ unidades |
| **Oferta / bundle** | BOFU | Packs reales de Releasit |
| **Reseñas / 5 estrellas** | BOFU | Fuentes: compradores reales (Shopify/Releasit/WhatsApp, con permiso), reseñas del mismo SKU en AliExpress traducidas, o testimonio guionizado en formato UGC. No capturas de "clientes" inventados con nombre y estrellas |
| **Carta de disculpa** | BOFU | Atada a algo real (lote agotado, demora real) o en tono creativo ("perdón, plantillas de gel") |
| **Poco stock / última hora** | BOFU | Atada a algo real: inventario del lote, promo con fecha de fin que sí se cumple |
| **No compres esto** (si…) | MOFU | "Para quién no es" |

## E. Video generado con IA (requiere herramienta de video conectada)
Claymation (plastilina), esqueleto IA, estilo Zack D Films 3D, objeto parlante animado, avatar UGC, podcast con avatar. **Sí van**, pero hoy no hay una herramienta de video conectada. Mientras tanto, en la matriz se marcan como "⏳ pendiente de herramienta" y se produce la versión con voz + fábrica + stock.

## Ángulos (lista de @keko_mkt, DbWsocPPw6P)
El dolor que resuelve · antes y después · lo que dice un cliente real · lo que dice un experto · por qué es distinto a la competencia · el mito desmentido · el error del que no lo usa · la objeción n.º 1 · para quién no es · precio por día · qué pasa a los 7, 14 y 30 días · cómo se hace · la rutina donde encaja · el regalo perfecto · qué pasa si no lo compras · la historia de por qué lo creamos · el material que nadie más usa · queda poco stock (solo si es verdad).

## Catálogo completo unificado (todos los formatos de los reels, sin repetir)
Une las listas de @_tomlewis (42, EN), @antonio.ferriani (30, PT), @keko_mkt (35), @etcheberritomartin (10), @bruno.dbenedetto (estáticos), @francogalvanads, @avatarhype y @diegodavila.ai. Leyenda: 🎙️ video con voz · 🎬 video sin voz · 🤖 video con IA (⏳ falta herramienta) · 🖼️ estático HTML · 📸 foto real o de fábrica.

**Video**
| Formato | Qué es | Producción |
|---|---|---|
| UGC | Creador casual hablando, parece un posteo de un amigo | 🎙️ voz + stock/fábrica · 🤖 avatar |
| Testimonio de cliente | "Me pasaba X…" en primera persona | 🎙️ |
| Testimonio en DM / caja de preguntas | Respuesta a un DM o a la caja de preguntas de IG | 🖼️ captura + 🎙️ |
| Podcast con IA / dualcast | Dos personas conversando del problema | 🎙️ dos voces · 🤖 avatares |
| Voz en off | Narración sobre b-roll | 🎙️ |
| "Te voy a contar la verdad" | Confesión o desmentido | 🎙️ |
| Reacción | Alguien reacciona al producto o a un dato | 🤖 |
| Green screen | Persona delante de una captura (noticia, reseña, web) | 🤖 · 🖼️ fondo |
| ASMR | Sonido de uso, manos, nativo | 🎬 fábrica |
| Tipo TikTok / nativo | Cortes de 1 s, texto nativo | 🎬 |
| Stories natural | Video vertical casero con la tipografía de IG | 🎬 |
| Macro con textos | Producto de cerca + 3 textos + tarjeta | 🎬 |
| Mockup del producto | Producto girando o en uso, limpio | 🎬 fábrica · 🤖 |
| Objeto parlante | El producto habla | 🎙️ + 🤖 |
| Pizarra / whiteboard | Mano dibujando el mecanismo | 🤖 · 🖼️ animado |
| Garabato / doodle | Dibujos simples sobre el video | 🖼️ overlay |
| Transformación / evolución | Antes → después mostrado, no explicado | 📸 real |
| Problema + quiz | "¿Te pasa esto? Responde…" | 🎙️ + 🖼️ |
| Claymation / esqueleto IA / Zack D Films 3D | Animación que rompe el patrón | 🤖 |
| Se busca ("procura-se") | Cartel de "SE BUSCA: gente con dolor de…" | 🖼️ |
| Atención / advertencia | Abre con alerta roja | 🖼️ · 🎙️ |

**Estático nativo** (parece contenido, no anuncio)
| Formato | Qué es |
|---|---|
| Historia de Instagram | Foto casera + tipografía de IG |
| Nota del iPhone | Lista con checks |
| Captura de chat / WhatsApp / mensaje de texto | Conversación que recomienda |
| Llamada perdida / notificación | "Llamada perdida: tus pies" |
| Búsqueda de Google | La pregunta del dolor en el buscador |
| Captura de email | "Tu pedido va en camino" / "pedimos disculpas" |
| Ticket de compra | Recibo con el pack y el total real |
| Imagen de Paint / ugly ad | Foto de celular con texto mal puesto |
| Texto a mano / texto sobre la piel | Escrito en papel o en la piel (pie, mano) |
| Texto sobre pantalla negra | Solo texto, blanco sobre negro |
| Meme | Plantilla de meme con el problema |
| Estilo Reddit / X | Pregunta + respuestas |
| Breaking news / titular de noticia | Abre con novedad o curiosidad |
| Pantalla dividida | Dos mitades comparadas |

**Estático de argumento**
| Formato | Qué es |
|---|---|
| Punteo de beneficios | Bullets que se leen en 2 s ("el más subestimado") |
| Títulos creativos | La primera línea hace todo el trabajo |
| X razones por las que… / X señales de que… | Lista numerada |
| Nosotros vs. ellos / comparativa | Contra la alternativa genérica |
| Nosotros vs. nosotros | Versión vieja vs. nueva del propio producto |
| Lo nuevo vs. lo viejo / lo que tenés vs. lo que podés tener | Lado a lado |
| Problema vs. solución | Dos columnas |
| Problemas tachados / lo que podés evitar | Lista de dolores tachados |
| Diagrama / Venn | Mecanismo o "lo mejor de dos mundos" |
| Tier list | Ranking de alternativas, el producto arriba |
| Mito vs. realidad | Objeción desmentida |
| Efecto secundario | "Efectos secundarios: terminar el día sin dolor…" (ironía) |
| En caso de emergencia | "Rompa el vidrio" con el producto |
| No compres esto / no seas ese que… / don't be an idiot | Reverso, provoca |
| Hack 101 | Truco rápido con el producto |
| Titular con dato / estadística | Cifra grande de los datos del producto |
| Reseñas / Trustpilot / cero estrellas | Prueba social; "cero estrellas" = ironía ("0 quejas") |

**Oferta y cierre (BOFU)**
| Formato | Qué es |
|---|---|
| Oferta / oferta combo (bundle) | Packs de Releasit, ahorro real |
| Precio por día | "Menos que un tinto al día" |
| Alerta de poco stock / última hora | Atada al lote o a la fecha de la promo |
| Pedimos disculpas / carta de disculpa | Atada a algo real o en tono creativo |
| Remarketing | Para quien ya vio o visitó: objeción + oferta |

## Estructura de un anuncio: gancho → cuerpo → CTA

**1. Gancho (0–3 s).** Decide si se ve el resto. Tiene **3 capas que dicen lo mismo**: la imagen del primer fotograma, el texto en pantalla y la primera frase de la voz. Tipos de gancho (se rota el tipo, no solo las palabras):
| Tipo | Ejemplo |
|---|---|
| Dolor en primera persona | "Me dolía la cadera al final del día" |
| Pregunta de dolor | "¿Cuántas plantillas ha comprado que a la semana ya están aplastadas?" |
| Instrucción / prueba casera | "Mira la huella de tu hijo después de bañarse" |
| Novedad / noticia | "Descubrieron por qué te duele la cadera aunque no hagas ejercicio" |
| Contraintuitivo / mito | "La plantilla blandita es la que más te está dañando" |
| Reverso | "No compres plantillas hasta ver esto" |
| Identidad | "Si trabajas de pie más de 8 horas…" |
| Dato | "237 piezas en un maletín" |
| Ruptura visual | Primer fotograma raro: claymation, macro extremo, texto en la piel |
Reglas: un solo ángulo por gancho; nada de logo ni "compra ya" en los primeros 3 s; el texto se lee sin sonido.

**2. Cuerpo (3–18 s).** Lleva este orden, y cada bloque es una frase con su escena:
1. **Agitar:** qué pasa si sigue el problema.
2. **Mecanismo:** por qué funciona ("arco firme que no se aplasta + copa de talón").
3. **Prueba:** demostración, material o cifra del producto (lo que no se ve no se cree).
4. **Objeción n.º 1:** "va en cualquier zapato", "desde la talla 35", "sin pantallas".
Cada escena tiene que mostrar lo que dice la frase (ver QA en `montaje-ffmpeg.md`).

**3. CTA (últimos 3–5 s).** Tiene 3 partes:
1. **Oferta concreta:** pack y precio reales ("2 unidades por $X").
2. **Riesgo cero:** envío gratis y pago contra entrega.
3. **Instrucción:** "Pídela aquí abajo 👇", con la tarjeta final de 3 s y el botón SHOP_NOW.

Duración: con voz, 18–25 s; macro, ~10 s.

## Cómo iterar
1. **RECON** (arriba): 4 ángulos × ganchos con gasto parejo, durante 5–7 días.
2. **Qué cambiar según la métrica** (embudo de `/one-cbo`):
   - CTR < 1 % o hook rate bajo → **gancho nuevo**, mismo cuerpo.
   - Hook bien pero se van a mitad (hold rate bajo) → **cuerpo**: más corto, prueba antes, menos explicación.
   - CTR alto y no compran → **CTA, oferta o landing**, no el video.
   - CPA bien → **no tocar**; duplicar y sumar variaciones al lado.
3. **Multiplicar al ganador:** 6 ganchos nuevos sobre el mismo cuerpo + el mismo ángulo en 6 formatos (por ejemplo: UGC → nota del iPhone → nosotros vs. ellos → macro → podcast → oferta combo).
4. **Cada semana:** 15 creativos nuevos como mínimo, con al menos un ángulo nuevo. Se pausa lo que lleva 3–7 días sin vender y se dejan las piezas TOFU aunque su CPA sea más alto.
5. **Nombre de cada anuncio**, para leer por ángulo y por formato en Meta: `PRODUCTO_ANGULO_FORMATO_GANCHO_v` → `PROD_DOLOR_UGC_H1_v1`, `PROD_IDENT_NOTAIPHONE_H2_v1`.

## Herramienta de Meta anotada
**Entrega push del anuncio** (@bruno.dbenedetto, DZdoJ2VtlY8): a nivel de anuncio, bajo "anuncios multianunciante", hay un interruptor que asigna un % del presupuesto diario para garantizar que un anuncio nuevo se muestre (de 1 a 30 días). Sirve para que la CBO no deje sin gasto a los creativos nuevos. Solo en algunas cuentas; con varios anuncios a la vez puede no cumplir el mínimo. Falta revisar si se puede activar por API.

## Referencias
| ID | Cuenta | Qué aporta |
|---|---|---|
| DeQJziWpPqh | @francogalvanads | Titular de noticia, ugly ads, historia de IG |
| Ddt1H_vlJlV | @jhonhmastery | Carrusel "SBB" (no descargado: imágenes) |
| DdeaRYfFC4v | @jhonhmastery | TOFU: no se apaga aunque venda caro |
| Db8pB-BIkH6 | @_tomlewis | Lista de 42 formatos (EN) |
| DbWeBUIve3k | @antonio.ferriani | Lista de 30 formatos (PT) |
| DcHWBxIPHF- | @bruno.dbenedetto | Estáticos: carta de disculpa, tenés vs. podés tener, ticket, llamada perdida, notas, Paint |
| Db4xGlWsKU9 | @diegodavila.ai | Animados IA (esqueleto, claymation, objeto parlante) |
| DZ_MiA_M_G_ | @avatarhype | Volumen: 10+ anuncios por semana; podcast, dualcast, voz en off |
| DbUOUBHPjhj | @keko_mkt | 35 formatos (lista en pantalla) |
| DbWsocPPw6P | @keko_mkt | 18 ángulos |
| DabeIKcPiwu | @etcheberritomartin | 10 formatos explicados |
| DZdoJ2VtlY8 | @bruno.dbenedetto | Entrega push |
| DY4oyi2Oq6h | @burgielias | Ángulo × formato, diversidad creativa |
| DcFEBOaOktc | @davidaistar | Skill de Claude, no es formato (no se descargó) |
