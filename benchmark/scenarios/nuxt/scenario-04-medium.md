# Scenario: Blog with Comments and Auth

## Difficulty
Medium

## Description
Implement a blog system with posts, comments, auth middleware, and full 2-layer architecture.

## Prompt
Create Post and Comment domain entities with 6 branded types (PostId, CommentId, UserId, Title, Slug, Content). Implement a CommentPolicy interface with 2 implementations: PublicComments, ModeratedComments. Create domain services: createPost, addComment, moderateComment. Create auth middleware that injects user into context. Create 4 Vue components: PostList, PostDetail, CommentList, CommentForm. Create 3 server API routes: posts.get, posts.post, comments.post. Domain pure TypeScript.

## Expected Output
- File: `domain/entity/post.ts`, `domain/entity/comment.ts`, `domain/entity/types.ts`, `domain/policy/commentPolicy.ts`, `domain/service/blogService.ts`, `server/api/*.ts`, `components/*.vue`, `composables/useBlog.ts`
- Must contain: 2 entities, 6 branded types, policy interface + 2 impls, 3 services, auth middleware, 4 components, 3 API routes
- Must not contain: `any`, domain logic in components, Nuxt imports in domain

## Scoring Criteria
- [ ] SRP: Entities, policy, services, components each separate (15 points)
- [ ] Naming: 6 branded types, descriptive names (10 points)
- [ ] Type safety: No any, typed middleware, branded types (15 points)
- [ ] 2-layer: Policy pattern, middleware, server routes (20 points)
- [ ] Domain purity: Zero Nuxt/Vue in domain (20 points)
- [ ] Architecture: Auth middleware, proper data flow (20 points)
