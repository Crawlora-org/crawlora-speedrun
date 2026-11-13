import type {
  CrawloraGeneratedGroups,
  OperationId,
  OperationParamsMap,
  OperationRequestArgs,
  OperationResponseMap
} from "./types.js";

export type CrawloraParams = Record<string, unknown>;
export type CrawloraLogEvent = { event: string; [key: string]: unknown };
export interface CrawloraRequestContext { operationId: string; method: string; url: string; headers: Record<string, string> }
export type CrawloraBeforeRequest = (ctx: CrawloraRequestContext) => void | Promise<void>;
export type CrawloraAfterResponse = (operationId: string, status: number, headers: Record<string, string>, body: unknown) => unknown;

export interface CrawloraClientOptions {
  apiKey?: string;
  jwtToken?: string;
  baseUrl?: string;
  timeout?: number;
  retries?: number;
  retryDelay?: number;
  maxRetryDelay?: number;
  retryStatuses?: Iterable<number>;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
  onRetry?: (attempt: number, error: CrawloraError, delay: number) => void;
  requestId?: boolean;
  idempotencyKeys?: boolean;
  rateLimit?: number;
  maxConcurrency?: number;
  logger?: (event: CrawloraLogEvent) => void;
  beforeRequest?: CrawloraBeforeRequest | Iterable<CrawloraBeforeRequest>;
  afterResponse?: CrawloraAfterResponse | Iterable<CrawloraAfterResponse>;
  headers?: Record<string, string>;
  userAgent?: string | false;
  fetch?: typeof globalThis.fetch;
}

export interface CrawloraRequestOptions {
  headers?: Record<string, string>;
  responseType?: "auto" | "json" | "text" | "stream";
  timeout?: number;
  signal?: AbortSignal;
  retries?: number;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
}

export interface OperationDefinition {
  id: string; method: string; path: string; pathParams: string[];
  queryParams: Array<{ name: string; in?: "query"; collectionFormat?: string; type?: string; required?: boolean; enum?: string[] }>;
  formParams: Array<{ name: string; in?: "formData"; type?: string; required?: boolean; enum?: string[] }>;
  bodyParam?: string; bodyRequired?: boolean; consumes: string[]; produces: string[]; security: string[];
  paginatable?: boolean; cursorParams?: string[];
}

export class CrawloraError extends Error {
  status: number; code?: number; body: unknown; headers: Record<string, string>;
  response?: Response; cause?: unknown; retryable?: boolean; requestId?: string;
}
export class CrawloraClientError extends CrawloraError {}
export class CrawloraServerError extends CrawloraError {}
export class CrawloraNetworkError extends CrawloraError {}

export interface CrawloraPaginateOptions extends CrawloraRequestOptions {
  pageParam?: string; cursorParam?: string; nextCursor?: (page: unknown) => unknown;
  start?: unknown; step?: number; maxPages?: number;
}
export interface CrawloraPaginateItemsOptions extends CrawloraPaginateOptions {
  items?: (page: unknown) => Iterable<unknown>;
}

export class CrawloraClient {
  constructor(options?: CrawloraClientOptions);
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  paginate<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateOptions): AsyncGenerator<OperationResponseMap[I], void, unknown>;
  paginateItems<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateItemsOptions): AsyncGenerator<unknown, void, unknown>;
  [group: string]: unknown;
}
export interface CrawloraClient extends CrawloraGeneratedGroups {}

export class SpeedrunClient extends CrawloraClient {
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  catalog(params: OperationParamsMap["speedrun-catalog"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  categoryDetail(params: OperationParamsMap["speedrun-category-detail"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  categoryRecords(params: OperationParamsMap["speedrun-category-records"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  categoryVariables(params: OperationParamsMap["speedrun-category-variables"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  games(params?: OperationParamsMap["speedrun-games"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  gameDetail(params: OperationParamsMap["speedrun-game-detail"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  categories(params: OperationParamsMap["speedrun-categories"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  levels(params: OperationParamsMap["speedrun-levels"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  records(params: OperationParamsMap["speedrun-records"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  variables(params: OperationParamsMap["speedrun-variables"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  gameLeaderboard(params: OperationParamsMap["speedrun-game-leaderboard"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  levelLeaderboard(params: OperationParamsMap["speedrun-level-leaderboard"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  levelDetail(params: OperationParamsMap["speedrun-level-detail"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  levelCategories(params: OperationParamsMap["speedrun-level-categories"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  levelRecords(params: OperationParamsMap["speedrun-level-records"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  levelVariables(params: OperationParamsMap["speedrun-level-variables"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  resourceOptions(params?: OperationParamsMap["speedrun-resource-options"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  runs(params?: OperationParamsMap["speedrun-runs"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  runsOptions(params?: OperationParamsMap["speedrun-runs-options"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  run(params: OperationParamsMap["speedrun-run"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  catalog(params: OperationParamsMap["speedrun-catalog"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  categoryDetail(params: OperationParamsMap["speedrun-category-detail"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  categoryRecords(params: OperationParamsMap["speedrun-category-records"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  categoryVariables(params: OperationParamsMap["speedrun-category-variables"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  games(params?: OperationParamsMap["speedrun-games"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  gameDetail(params: OperationParamsMap["speedrun-game-detail"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  categories(params: OperationParamsMap["speedrun-categories"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  levels(params: OperationParamsMap["speedrun-levels"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  records(params: OperationParamsMap["speedrun-records"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  variables(params: OperationParamsMap["speedrun-variables"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  gameLeaderboard(params: OperationParamsMap["speedrun-game-leaderboard"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  levelLeaderboard(params: OperationParamsMap["speedrun-level-leaderboard"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  levelDetail(params: OperationParamsMap["speedrun-level-detail"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  levelCategories(params: OperationParamsMap["speedrun-level-categories"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  levelRecords(params: OperationParamsMap["speedrun-level-records"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  levelVariables(params: OperationParamsMap["speedrun-level-variables"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  resourceOptions(params?: OperationParamsMap["speedrun-resource-options"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  runs(params?: OperationParamsMap["speedrun-runs"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  runsOptions(params?: OperationParamsMap["speedrun-runs-options"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  run(params: OperationParamsMap["speedrun-run"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;

  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  catalog(...args: OperationRequestArgs<"speedrun-catalog">): Promise<OperationResponseMap["speedrun-catalog"]>;
  categoryDetail(...args: OperationRequestArgs<"speedrun-category-detail">): Promise<OperationResponseMap["speedrun-category-detail"]>;
  categoryRecords(...args: OperationRequestArgs<"speedrun-category-records">): Promise<OperationResponseMap["speedrun-category-records"]>;
  categoryVariables(...args: OperationRequestArgs<"speedrun-category-variables">): Promise<OperationResponseMap["speedrun-category-variables"]>;
  games(...args: OperationRequestArgs<"speedrun-games">): Promise<OperationResponseMap["speedrun-games"]>;
  gameDetail(...args: OperationRequestArgs<"speedrun-game-detail">): Promise<OperationResponseMap["speedrun-game-detail"]>;
  categories(...args: OperationRequestArgs<"speedrun-categories">): Promise<OperationResponseMap["speedrun-categories"]>;
  levels(...args: OperationRequestArgs<"speedrun-levels">): Promise<OperationResponseMap["speedrun-levels"]>;
  records(...args: OperationRequestArgs<"speedrun-records">): Promise<OperationResponseMap["speedrun-records"]>;
  variables(...args: OperationRequestArgs<"speedrun-variables">): Promise<OperationResponseMap["speedrun-variables"]>;
  gameLeaderboard(...args: OperationRequestArgs<"speedrun-game-leaderboard">): Promise<OperationResponseMap["speedrun-game-leaderboard"]>;
  levelLeaderboard(...args: OperationRequestArgs<"speedrun-level-leaderboard">): Promise<OperationResponseMap["speedrun-level-leaderboard"]>;
  levelDetail(...args: OperationRequestArgs<"speedrun-level-detail">): Promise<OperationResponseMap["speedrun-level-detail"]>;
  levelCategories(...args: OperationRequestArgs<"speedrun-level-categories">): Promise<OperationResponseMap["speedrun-level-categories"]>;
  levelRecords(...args: OperationRequestArgs<"speedrun-level-records">): Promise<OperationResponseMap["speedrun-level-records"]>;
  levelVariables(...args: OperationRequestArgs<"speedrun-level-variables">): Promise<OperationResponseMap["speedrun-level-variables"]>;
  resourceOptions(...args: OperationRequestArgs<"speedrun-resource-options">): Promise<OperationResponseMap["speedrun-resource-options"]>;
  runs(...args: OperationRequestArgs<"speedrun-runs">): Promise<OperationResponseMap["speedrun-runs"]>;
  runsOptions(...args: OperationRequestArgs<"speedrun-runs-options">): Promise<OperationResponseMap["speedrun-runs-options"]>;
  run(...args: OperationRequestArgs<"speedrun-run">): Promise<OperationResponseMap["speedrun-run"]>;
}
export { SpeedrunClient as Client };
export const operations: Record<string, OperationDefinition>;
export const groups: Record<string, Record<string, string>>;
export const operationCount: number;
export const OperationIds: Readonly<Record<string, OperationId>>;
export const VERSION: string;
export * from "./types.js";
export default SpeedrunClient;
