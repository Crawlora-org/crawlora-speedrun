import { SpeedrunClient } from "../src/index.js";

const client = new SpeedrunClient({ apiKey: "test-key" });
void client.catalog({"kind": "platforms"});
void client.request("speedrun-catalog", {"kind": "platforms"});
const streamResponse: Promise<Response> = client.request("speedrun-catalog", {"kind": "platforms"}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("speedrun-catalog", {"kind": "platforms"}, { responseType: "stream" });
const directStream: Promise<Response> = client.catalog({"kind": "platforms"}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("speedrun-catalog", {"kind": "platforms", "max": 1, "offset": 1}, { responseType: "text" });
const rawText: Promise<string> = client.request("speedrun-catalog", {"kind": "platforms"}, { responseType: "text" });
void rawText;


void client.games();
void client.request("speedrun-games");
// @ts-expect-error The selected operation requires its documented params.
void client.catalog();
