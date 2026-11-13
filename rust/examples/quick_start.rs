use crawlora_speedrun::{Client, ModelSpeedrunResponseDoc, SpeedrunGamesParams};

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
