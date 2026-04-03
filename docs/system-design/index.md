# System Design

## Scalability

- **Vertical scaling**: bigger machine (more CPU/RAM). Simple but has a ceiling.
- **Horizontal scaling**: more machines. Requires stateless services, load balancing.

## Load Balancing

Distributes requests across servers. Strategies: round-robin, least connections, IP hash (sticky sessions).
- L4 (TCP level) — fast, no content awareness
- L7 (HTTP level) — route by URL, headers, cookies

## Caching

Store expensive computation results closer to the consumer.

| Layer | Example | Trade-off |
|-------|---------|-----------|
| In-memory (process) | LRU cache | Lost on restart |
| Distributed cache | Redis, Memcached | Network hop, consistency |
| CDN | CloudFront | Great for static assets |

**Cache invalidation** is the hard part: TTL, write-through, write-behind, cache-aside.

## Consistency vs Availability

- **Strong consistency**: every read returns the latest write. Requires coordination (slow).
- **Eventual consistency**: reads may return stale data, but converge over time. Faster, more available.

## CAP Theorem

In a distributed system, you can only guarantee two of three:

- **Consistency** — every node returns the same data
- **Availability** — every request gets a response
- **Partition tolerance** — system works despite network splits

In practice: partitions happen. You choose CP (consistency over availability) or AP (availability over consistency).

## Latency vs Throughput

- **Latency**: time for a single request (ms). Optimize: caching, faster queries, co-location.
- **Throughput**: requests per second. Optimize: horizontal scaling, async processing, batching.

## Queues & Pub/Sub

- **Queue** (point-to-point): producer sends, one consumer receives. Use for: async job processing, decoupling services. Examples: SQS, RabbitMQ.
- **Pub/Sub**: producer publishes to topic, many subscribers receive. Use for: event-driven architectures, fan-out. Examples: Kafka, SNS.
