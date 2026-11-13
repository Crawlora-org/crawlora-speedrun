# Crawlora Speedrun.com Rust SDK

[![Crates.io](https://img.shields.io/crates/v/crawlora-speedrun.svg)](https://crates.io/crates/crawlora-speedrun)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Official async Rust client for Crawlora's hosted Speedrun.com API. It exposes
typed request parameters and response handling for 20 public
operations. It calls Crawlora's hosted service; it does not scrape Speedrun.com
locally. Requests use your Crawlora account and follow its billing plan. Crawlora
is independent from and not affiliated with or endorsed by Speedrun.com or
its owners.

[Crawlora](https://crawlora.net?utm_source=crates.io&utm_medium=referral&utm_campaign=platform-clients&utm_content=speedrun-rust-homepage) ·
[API documentation](https://crawlora.net/docs?utm_source=crates.io&utm_medium=referral&utm_campaign=platform-clients&utm_content=speedrun-rust-api-docs) ·
[Pricing](https://crawlora.net/pricing?utm_source=crates.io&utm_medium=referral&utm_campaign=platform-clients&utm_content=speedrun-rust-pricing) ·
[Create an account](https://crawlora.net/signup?utm_source=crates.io&utm_medium=referral&utm_campaign=platform-clients&utm_content=speedrun-rust-signup)

- **Rust:** 1.88 or newer
- **Async runtime:** Tokio
- **Authentication:** Crawlora API key (`x-api-key`)
- **Operations:** [Rust reference](docs/operations.md) · [all endpoints and parameters](https://github.com/Crawlora-org/crawlora-speedrun/blob/main/docs/usage.md)

## Install

```sh
cargo add crawlora-speedrun
```

To pin a release directly in `Cargo.toml`:

```toml
[dependencies]
crawlora-speedrun = "0.1.0"
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=crates.io&utm_medium=referral&utm_campaign=platform-clients&utm_content=speedrun-rust-signup), then [create an API key](https://crawlora.net/app/api-keys?utm_source=crates.io&utm_medium=referral&utm_campaign=platform-clients&utm_content=speedrun-rust-api-keys). Keep the key out of source control and load it from the environment:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Quick start

```rust,no_run
use crawlora_speedrun::{Client, SpeedrunGamesParams, ModelSpeedrunResponseDoc};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = std::env::var("CRAWLORA_API_KEY")?;
    let client = Client::new(api_key)?;
    let response = client
        .speedrun
        .games(SpeedrunGamesParams {
            name: Some("Super Mario 64".to_owned()),
            max: Some(5),
            ..Default::default()
        })
        .await?;
    let data: ModelSpeedrunResponseDoc = response.into_json()?;
    println!("{data:#?}");
    Ok(())
}
```

Endpoint methods return the complete HTTP response. Use `into_json()` to decode
JSON into `serde_json::Value` or a generated response model. The response also
preserves headers and status; text and byte response modes are available through
`RequestOptions`.

## Configuration and errors

`CrawloraClient::builder()` supports a custom API base URL, timeout, retry limit,
default headers, JWT authentication, and a custom HTTP client. Retry behavior is
bounded and honors `Retry-After`. API failures are returned as `Error::Api` with
the HTTP status, response body, and request ID when provided.

## More resources

- Read the [generated Rust operation reference](docs/operations.md).
- Browse the [complete endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-speedrun/blob/main/docs/usage.md).
- Review the [hosted API documentation](https://crawlora.net/docs?utm_source=crates.io&utm_medium=referral&utm_campaign=platform-clients&utm_content=speedrun-rust-api-docs) and [pricing](https://crawlora.net/pricing?utm_source=crates.io&utm_medium=referral&utm_campaign=platform-clients&utm_content=speedrun-rust-pricing).

## License

MIT. See [LICENSE](LICENSE).
