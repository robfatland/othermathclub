# API Gateway Throttling

## Motivation

The Torus Mare API Gateway URL is published in this repository. Since the repo is public on GitHub, anyone who finds the URL can send requests to the endpoint. Without throttling, a malicious actor or bot could flood the API with thousands of requests per second, generating AWS charges (API Gateway costs $1 per million requests; Lambda has a free tier but charges beyond it).

A classroom of ~20 students playing an exploration game generates at most a few requests per second. There is no legitimate reason for the endpoint to serve traffic at datacenter scale.

## Implementation

A route-level throttle is applied to the `POST /` route on the API Gateway `$default` stage:

- **Rate limit**: 10 requests per second (steady state)
- **Burst limit**: 50 requests (short burst capacity)

This was configured with:

```bash
aws apigatewayv2 update-stage \
  --api-id j2m1oh7g1d \
  --stage-name '$default' \
  --route-settings '{"POST /":{"ThrottlingBurstLimit":50,"ThrottlingRateLimit":10}}' \
  --profile u0027 \
  --region us-west-2
```

## Consequences

### What this prevents

- Cost runaway from automated abuse (worst-case monthly cost at sustained 10 RPS ≈ $26, versus $26,000+ without throttling)
- Denial-of-service conditions that could degrade experience for students during a session

### What this does NOT affect

- Normal classroom usage (20 students × 1 request every few seconds = well under 10 RPS aggregate)
- The game experience during club meetings — 50-burst capacity handles the case where everyone hits Enter at the same time

### How students experience throttling

If a student somehow exceeds the limit (e.g., a runaway loop in their code), API Gateway returns HTTP 429 (Too Many Requests). The client helper should handle this gracefully by printing a "slow down" message and retrying after a pause.

### Adjusting later

To raise or lower the limits:

```bash
aws apigatewayv2 update-stage \
  --api-id j2m1oh7g1d \
  --stage-name '$default' \
  --route-settings '{"POST /":{"ThrottlingBurstLimit":NEW_BURST,"ThrottlingRateLimit":NEW_RATE}}' \
  --profile u0027 \
  --region us-west-2
```
