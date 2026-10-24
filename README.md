# cod-creativos

Plugin de **Claude Code** para tiendas de e-commerce **contraentrega (COD)** en Shopify que pautan en Meta. Hace el trabajo creativo de punta a punta:

1. **Investigación de anuncios** — Meta Ad Library (API + navegador), TikTok, AliExpress, Mercado Libre y landings extranjeras. Gemelos exactos verificados con fotogramas, descarga de videos de referencia, bancos de ángulos, ofertas y plan de testeo, y una investigación creativa completa publicada como Artifact.
2. **Landing en Shopify** — packshot fiel con Codex, 7 piezas verticales por estilo de categoría, portada con precios, GIFs del proveedor, packs de cantidad en el formulario contraentrega y revisión en celular.
3. **Videos con voz** — guiones por referencia, un avatar con su propia voz por guion (VoxCPM2, actuada frase por frase y validada con whisper), música original, b-roll de fábrica y de stock, montaje con ffmpeg y subida a Meta por API.

Funciona con cualquier tienda: cada usuario corre el setup y configura la suya.

## Instalación

En Claude Code:
```
/plugin marketplace add davis7448/cod-creativos
/plugin install cod-creativos@cod-creativos
```
Reinicia Claude Code y escribe **"configura mi tienda"** (skill `setup-creativos`). El setup:
- crea `CONFIG-TIENDA.md` en tu carpeta de trabajo (por defecto `~/ads-invest`) con tu marca, país, moneda, Shopify, IDs de Meta, fletes y preferencias, sacando lo que pueda de los conectores;
- revisa e instala (con tu permiso) las herramientas.

## Requisitos

| Herramienta | Para qué | Cómo |
|---|---|---|
| Claude Code | todo | claude.com/claude-code |
| Conector **Meta Ads** (claude.ai) | Ad Library, campañas, subida de anuncios | claude.ai → Configuración → Conectores |
| Conector **Shopify** (claude.ai) | productos, archivos, landing | claude.ai → Configuración → Conectores |
| MCP de **Playwright** | investigación en el navegador, capturas, portadas | `claude mcp add playwright -- npx @playwright/mcp@latest` |
| **ffmpeg** | montaje, GIFs, hojas de fotogramas | `brew install ffmpeg` |
| **Codex CLI** | packshot y piezas de la landing | `npm i -g @openai/codex` + `codex login` |
| **VoxCPM2** (`mlx-audio`, Python 3.11) | voces por avatar | ver `skills/ads-invest/references/voces-voxcpm2.md` (Mac con chip Apple) |
| **mlx-whisper + librosa** (otro entorno; incluye OmniVoice de respaldo) | validación del guion, tono y género de la voz | ver `skills/ads-invest/references/voces-omnivoice.md` |
| Stock licenciado (opcional) | b-roll de contexto | p. ej. conector de Magnific/Freepik |
| Plugin **cod-ops** (opcional) | contabilidad, One CBO, logística | `/plugin marketplace add davis7448/cod-ops` |

## Uso

Escríbele a Claude en lenguaje natural:
- *"Investiga el producto <link o fotos>"* → `ads-invest`
- *"Siguiente ronda de investigación de X"*
- *"Monta la landing de X"* → `landing-cod`
- *"Haz 4 videos con voz para X"* → `ads-invest` (Regla 5)
- *"Sube los videos a Meta"* → por API, siempre con tu visto bueno

## Reglas que trae de fábrica
- Verificar el producto real antes de investigar, y los gemelos con fotogramas.
- Videos de competidores o creadores = referencia, **nunca** b-roll pagado. Solo material del proveedor o la fábrica, stock licenciado, Codex o lo que grabes tú.
- Sin precios "antes" ficticios ni claims de salud sin respaldo.
- Nada se publica en Meta ni se activa en Shopify sin tu confirmación.

## Privacidad
El plugin no trae datos de ninguna tienda. Tu `CONFIG-TIENDA.md` y tu carpeta de trabajo se quedan en tu equipo: no los subas a un repositorio público.

## Estructura
```
.claude-plugin/        plugin.json y marketplace.json
skills/
  setup-creativos/     configuración de la tienda y de las herramientas
  ads-invest/          investigación + producción de videos (references/, scripts/, templates/, extension/)
  landing-cod/         landing en Shopify
templates/
  CONFIG-TIENDA.md     plantilla de configuración
```

## Licencia
MIT
