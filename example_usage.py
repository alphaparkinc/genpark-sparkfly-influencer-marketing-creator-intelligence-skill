from client import SparkFlyClient

def main():
    print("=" * 65)
    print("=== Testing SparkFly Creator & Influencer Marketing Skill ===")
    print("=" * 65)
    client = SparkFlyClient()

    # 1. Search creators for consumer tech campaign
    print("\n1. Querying verified TikTok creators in US...")
    creators = client.search_creators(
        platform="tiktok",
        category="consumer_tech",
        country="US",
        min_followers=50000,
        max_followers=500000
    )
    for c in creators:
        print(f"  -> Creator: {c['name']} ({c['handle']}) | Followers: {c['followers']:,}")
        print(f"     Engagement: {c['engagement_rate_pct']}% | Rate: ${c['rate_card_estimate_usd']} | SparkFly Score: {c['sparkfly_influence_score']}")

    # 2. Generate creative brief
    print("\n2. Generating viral short-form creative brief...")
    brief = client.generate_campaign_brief(
        brand_name="GenPark AI",
        product_name="Agentic Commerce Assistant",
        target_regions=["US", "UK", "DE"],
        key_talking_points=["Autonomous price tracking", "One-click checkout", "Multi-model reasoning"],
        total_budget_usd=10000.00
    )
    print(f"  -> Brief ID: {brief['brief_id']} (Status: {brief['status']})")
    print(f"  -> Suggested Hook: \"{brief['suggested_hooks'][0]}\"")
    print(f"  -> Creator Allocation: ${brief['budget_allocation_usd']['creator_fees']}")

    # 3. Model campaign ROI
    print("\n3. Modeling campaign ROI attribution...")
    roi = client.estimate_campaign_roi(budget_usd=10000.00, target_platform="tiktok", expected_creators_count=6)
    print(f"  -> Est. Impressions: {roi['estimated_impressions']:,}")
    print(f"  -> Forecasted GMV: ${roi['forecasted_gmv_usd']:,} (ROAS: {roi['estimated_roas']}x)")

    print("\n✓ SparkFly Creator Intelligence Skill test passed successfully!")

if __name__ == "__main__":
    main()
