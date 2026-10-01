import json, sys
from client import SparkFlyClient

def run_mcp_server():
    client = SparkFlyClient()
    manifest = {
        "mcp_version": "1.0.0",
        "protocol": "Model Context Protocol",
        "skill": "genpark-sparkfly-influencer-marketing-creator-intelligence-skill",
        "description": "SparkFly (Tec-Do) Creator Intelligence for Influencer Sourcing & Attribution",
        "supported_tools": [
            {
                "name": "search_creators",
                "description": "Searches high-engagement TikTok/Instagram/YouTube creators with demographic filters.",
                "parameters": ["platform", "category", "country", "min_followers", "max_followers"]
            },
            {
                "name": "generate_campaign_brief",
                "description": "Generates localized short-video campaign creative brief with viral hooks.",
                "parameters": ["brand_name", "product_name", "target_regions", "key_talking_points", "total_budget_usd"]
            },
            {
                "name": "estimate_campaign_roi",
                "description": "Estimates expected impressions, clicks, GMV, and ROAS for creator campaign.",
                "parameters": ["budget_usd", "target_platform", "expected_creators_count"]
            }
        ],
        "status": "ACTIVE_LISTENING"
    }
    print(json.dumps(manifest, indent=2))

if __name__ == "__main__":
    run_mcp_server()
