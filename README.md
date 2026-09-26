# dagster-jev

## Français

Contrôle bloquant d’asset basé sur une question Jev.

Installez Dagster, émettez une métadonnée `content` lors de la matérialisation et ajoutez le contrôle aux `Definitions`. Une réponse incertaine échoue le contrôle.

## English

Blocking asset check driven by a Jev question.

Install `dagster>=1.11,<2`, add `@asset` materialization metadata `content`, and register `semantic_asset_check(my_asset, question="Is the review safe to publish?")` in Definitions asset_checks. An uncertain route fails the check for review.

## Español

Comprobación bloqueante de activos basada en una pregunta Jev.

Instale Dagster, emita metadatos `content` al materializar e incluya la comprobación en `Definitions`. Una respuesta incierta hace fallar la comprobación.

## Contract / Contrat / Contrato

`yes`, `no`, `review`, `failure`; threshold default `0.8`. `review` is a real undecided state. Empty or oversized input becomes `review`; transport or invalid-response errors become `failure`. The shared client caps input at 32 KiB, response at 100 KiB, timeout at 10 s and calls at 10,000 per process; YAML templates enforce their own input and response bounds. No raw input is logged by this project. User data goes to the TypeSafe Jev API.

FR : `review` exige une revue humaine ; `failure` signale une erreur. Le contenu est envoyé à l’API TypeSafe Jev.

ES: `review` requiere revisión humana; `failure` indica un error. El contenido se envía a la API TypeSafe Jev.

## TLS / TLS / TLS

FR : si votre installation Python ne trouve pas les certificats racines, définissez `SSL_CERT_FILE` vers un bundle CA valide (par exemple `certifi.where()`). Ne désactivez pas la vérification TLS.

EN: if Python cannot find root certificates, set `SSL_CERT_FILE` to a valid CA bundle (for example `certifi.where()`). Keep TLS verification enabled.

ES: si Python no encuentra los certificados raíz, defina `SSL_CERT_FILE` con un paquete CA válido (por ejemplo `certifi.where()`). Mantenga activa la verificación TLS.

## Development / Développement / Desarrollo

`python -m unittest discover -p "test_*.py" -v`

Platform / Plateforme / Plataforma: [Dagster documentation](https://docs.dagster.io/guides/test/asset-checks).

MIT license. Community project; not an official Dagster integration.
