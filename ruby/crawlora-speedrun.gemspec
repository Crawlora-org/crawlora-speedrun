require_relative "lib/crawlora/speedrun/version"

Gem::Specification.new do |spec|
  spec.name = "crawlora-speedrun"
  spec.version = Crawlora::Speedrun::VERSION
  spec.summary = "Speedrun.com API client for Crawlora (20 endpoints)"
  spec.description = "Ruby client for Crawlora's hosted Speedrun.com API. Covers game and category discovery, leaderboards, records, variables, and run metadata across 20 endpoints."
  spec.authors = ["Crawlora"]
  spec.license = "MIT"
  spec.required_ruby_version = ">= 2.6"
  spec.files = Dir["lib/**/*.rb", "README.md", "CHANGELOG.md", "LICENSE"]
  spec.require_paths = ["lib"]
  spec.homepage = "https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=speedrun-ruby-homepage"
  spec.metadata = { "source_code_uri" => "https://github.com/Crawlora-org/crawlora-speedrun", "documentation_uri" => "https://github.com/Crawlora-org/crawlora-speedrun/blob/main/ruby/README.md", "rubygems_mfa_required" => "true" }

end
