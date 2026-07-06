# Scenario: Blog Platform with Posts and Comments

## Difficulty
Medium

## Description
Implement a blog platform with Post and Comment aggregates, publishing workflow, and moderation.

## Prompt
Create Post and Comment aggregates. Implement a publishing workflow (draft → review → published → archived). Create a ModerationPolicy trait with implementations: AutoModeration, ManualModeration. Use domain events: PostPublished, CommentAdded, PostModerated. Implement a CommentModerationUseCase and a PublishPostUseCase with event publishing via EventPublisher port.

## Expected Output
- File: `src/domain/entity/post.rs`, `src/domain/entity/comment.rs`, `src/domain/policy/moderation_policy.rs`, `src/domain/event/*.rs`, `src/domain/port/event_publisher.rs`, `src/domain/usecase/*.rs`, `src/infrastructure/*.rs`
- Must contain: Post aggregate, Comment aggregate, 2 moderation policies, 3 event types, EventPublisher port, 2 use cases
- Must not contain: Axum in domain, moderation bypass, `unwrap()` in production paths

## Scoring Criteria
- [ ] SRP: Post, comment, moderation, events each separate (15 points)
- [ ] Naming: Descriptive names throughout (10 points)
- [ ] Type safety: Traits, Result, thiserror, no unwrap (15 points)
- [ ] 2-layer: Policy pattern, domain events (20 points)
- [ ] Domain purity: Zero Axum/SQLx in domain (20 points)
- [ ] Workflow: State transitions with validation (20 points)
