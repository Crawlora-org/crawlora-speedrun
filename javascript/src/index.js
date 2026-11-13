import { groups } from "./operations.js";
import {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
} from "./client.js";

export class SpeedrunClient extends CrawloraClient {
  constructor(options = {}) {
    super({ ...options, userAgent: options.userAgent ?? "crawlora-speedrun-js/0.1.0" });
    this["catalog"] = (...args) => this.request("speedrun-catalog", ...args);
    this["categoryDetail"] = (...args) => this.request("speedrun-category-detail", ...args);
    this["categoryRecords"] = (...args) => this.request("speedrun-category-records", ...args);
    this["categoryVariables"] = (...args) => this.request("speedrun-category-variables", ...args);
    this["games"] = (...args) => this.request("speedrun-games", ...args);
    this["gameDetail"] = (...args) => this.request("speedrun-game-detail", ...args);
    this["categories"] = (...args) => this.request("speedrun-categories", ...args);
    this["levels"] = (...args) => this.request("speedrun-levels", ...args);
    this["records"] = (...args) => this.request("speedrun-records", ...args);
    this["variables"] = (...args) => this.request("speedrun-variables", ...args);
    this["gameLeaderboard"] = (...args) => this.request("speedrun-game-leaderboard", ...args);
    this["levelLeaderboard"] = (...args) => this.request("speedrun-level-leaderboard", ...args);
    this["levelDetail"] = (...args) => this.request("speedrun-level-detail", ...args);
    this["levelCategories"] = (...args) => this.request("speedrun-level-categories", ...args);
    this["levelRecords"] = (...args) => this.request("speedrun-level-records", ...args);
    this["levelVariables"] = (...args) => this.request("speedrun-level-variables", ...args);
    this["resourceOptions"] = (...args) => this.request("speedrun-resource-options", ...args);
    this["runs"] = (...args) => this.request("speedrun-runs", ...args);
    this["runsOptions"] = (...args) => this.request("speedrun-runs-options", ...args);
    this["run"] = (...args) => this.request("speedrun-run", ...args);
  }
}

export { SpeedrunClient as Client };
export {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
};
export { groups, operations, operationCount, OperationIds } from "./operations.js";
export const VERSION = "0.1.0";
export default SpeedrunClient;
