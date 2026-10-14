# CONFIG-TIENDA

> La crea y la mantiene la skill `setup-creativos`. La leen `ads-invest` y `landing-cod` antes de trabajar.
> **No la subas a un repositorio público:** trae los IDs de tu tienda y de tus cuentas de anuncios.

## Tienda
| Campo | Valor |
|---|---|
| Marca | `<nombre de la tienda>` |
| Carpeta de trabajo | `~/ads-invest` |
| País principal | `<Colombia>` |
| Código de país (ISO) | `<CO>` |
| Moneda | `<COP>` |
| Idioma de los anuncios | `es` |
| Modelo de venta | contraentrega (COD) |

## Shopify
| Campo | Valor |
|---|---|
| Tienda (handle del admin) | `<mi-tienda>` (de `admin.shopify.com/store/<mi-tienda>`) |
| Dominio público | `<mitienda.com>` |
| Publication ID de la tienda online | `<gid://shopify/Publication/...>` |
| App del formulario contraentrega | `Releasit COD Form` |
| Tema | `Dawn` |
| Landing plantilla (gid) | `<opcional, la primera landing aprobada>` |

## Meta Ads
| Campo | Valor |
|---|---|
| Cuenta publicitaria (act_) | `<ID>` |
| Página de Facebook | `<ID>` |
| Cuenta de Instagram (instagram_user_id) | `<ID>` |
| Píxel / dataset | `<ID>` |
| Campaña One CBO activa | `<opcional>` |
| Presupuesto diario por defecto | `<opcional>` |

## Economía contraentrega
| Campo | Valor |
|---|---|
| Flete de envío por pedido | `<15500>` |
| Flete de devolución | `<igual al de envío>` |
| Tasa de despacho (pedidos que se despachan) | `0.80` |
| Tasa de entrega (despachados que se entregan) | `0.90` |
| Target CPA | `55–60 % del break-even` |

## Material para creativos
| Campo | Valor |
|---|---|
| Stock licenciado | `<Magnific/Freepik · Envato · ninguno>` |
| ¿El stock premium gasta créditos? | `<sí/no>` |
| Imágenes con IA | `Codex CLI` |
| Voces | `OmniVoice (~/.venvs/voz)` |

## Voces aprobadas
| Perfil | instruct | speed | Uso |
|---|---|---|---|
| D mamá | female, middle-aged, moderate pitch | 1.0 | testimonio |
| F hombre | male, young adult, moderate pitch | 1.15 | testimonio de papá |

## Preferencias del usuario
<!-- Cada corrección o decisión del usuario, con fecha. Ejemplos: -->
- Mostrar los videos antes de subirlos a Meta.
- Meta solo por API; no abrir los borradores en el editor.
- Nunca usar clips de competidores o creadores como b-roll.
