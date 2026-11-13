import { SpeedrunClient } from "../javascript/src/index.js";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new SpeedrunClient({ apiKey });

  const games = await client.games({ name: "Super Mario 64", max: 5 });
  console.log("games", games);
  const resourceOptions = await client.resourceOptions({  });
  console.log("resourceOptions", resourceOptions);
