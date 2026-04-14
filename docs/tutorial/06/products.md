# APIM Policy fragments

Remember the Token Limit quota policy we added to Both APIs? Imagine a business requirement like this

1. We want to give team A 10M tokens per day. But team B only 1M tokens per day.
1. We want team C to have no quota.

That can quickly turn into a complex set of APIs just for the sake of the policies.
