
---

# 🔹 BACKEND (FastAPI + REST)

## 1️⃣ FastAPI Request Lifecycle

> A request comes through ASGI, gets routed to the matching endpoint, dependencies are resolved first, then request data is validated using Pydantic.
> If validation passes, the endpoint logic runs and the response is serialized back through Pydantic before returning JSON.

---

## 2️⃣ Dependency Injection (DI)

> FastAPI uses dependency injection to manage shared logic like auth, DB sessions, and configs.
> It helps keep endpoints clean, improves testability, and avoids duplicated code across routes.

---

## 3️⃣ Request / Response Models (Pydantic)

> I use Pydantic models to validate incoming data and control outgoing responses.
> This ensures type safety, prevents invalid data from reaching business logic, and gives automatic API documentation.

---

## 4️⃣ Validation

> Validation is handled automatically using Pydantic schemas at the API boundary.
> This reduces runtime errors and ensures only well-structured data reaches the service layer.

---

## 5️⃣ Authentication (JWT / Sessions)

> I’ve integrated JWT-based auth using access tokens passed in headers.
> While deeper infra like token rotation was handled by the team, I understand token validation, expiry, and role-based access checks.

---

## 6️⃣ Pagination & Filtering

> I use limit–offset or cursor-based pagination depending on dataset size.
> Filtering is handled via query parameters and applied at the database query level for performance.

---

## 7️⃣ Error Handling

> I use centralized exception handling with HTTPException and custom error responses.
> This keeps API responses consistent and improves debugging and client-side error handling.

---

## 8️⃣ Why FastAPI over Django?

> FastAPI is faster to develop, async-friendly, and enforces validation by default.
> It’s ideal for API-first, high-performance systems, whereas Django is better for full-stack monoliths.

---

## 9️⃣ How Do You Structure Large APIs?

> I separate concerns into routers, services, schemas, and database layers.
> This keeps the codebase modular, scalable, and easy to maintain as features grow.

---

## 🔟 Sync vs Async in FastAPI

> Async endpoints are useful for I/O-bound tasks like external API calls.
> For CPU-heavy or blocking DB operations, I prefer sync to avoid unnecessary complexity.

---

# 🔹 DATABASE & PERFORMANCE (PostgreSQL)

## 1️⃣ PostgreSQL Indexing

> I add indexes on frequently filtered, joined, or sorted columns.
> Proper indexing significantly improves query performance, especially on large tables.

---

## 2️⃣ One-to-Many Relationships

> I use foreign keys with proper indexing to maintain integrity.
> This is common for user-to-orders or parent-child data structures.

---

## 3️⃣ Many-to-Many Relationships

> I use junction tables with foreign keys to both entities.
> This keeps data normalized and queries flexible.

---

## 4️⃣ Migrations

> I use migrations to safely evolve schemas without data loss.
> They help keep database changes versioned and consistent across environments.

---

## 5️⃣ N+1 Query Problem

> N+1 happens when queries are executed inside loops.
> I solve it using joins, prefetching, or optimized queries to reduce DB calls.

---

## 6️⃣ Pagination Strategies

> Offset pagination works for small datasets, but for large data I prefer cursor-based pagination.
> It’s more performant and avoids issues with shifting data.

---

## 7️⃣ Basic Query Optimization

> I analyze slow queries using EXPLAIN and logs.
> Then I optimize indexes, reduce joins, and avoid unnecessary data fetching.

---

## 8️⃣ Schema Design

> I design schemas based on access patterns, not just normalization.
> The goal is clarity, scalability, and efficient querying.

---

## 9️⃣ Improving Slow APIs

> I start by identifying bottlenecks—DB queries, serialization, or external calls.
> Then I optimize queries, add caching, and reduce response payload size.

---

## 🔟 Handling Large Datasets

> I avoid loading everything into memory.
> Pagination, background processing, and efficient querying are key to scalability.

---
Perfect 👍
Below are **simple, senior-style, 3–4 line answers** for **React questions**, exactly the way interviewers expect—clear, practical, and based on **real product experience like MyBitOfIt**.

You can **memorize these safely**.

---

# 🔹 REACT – CORE CONCEPTS

## 1️⃣ Functional Components

> I prefer functional components because they’re simpler, easier to test, and work naturally with hooks.
> They encourage cleaner logic separation and are now the standard approach in React.

---

## 2️⃣ useState

> `useState` is used for local component state.
> I keep state minimal and colocated close to where it’s used to reduce complexity and re-renders.

---

## 3️⃣ useEffect

> `useEffect` is used for side effects like API calls or subscriptions.
> I always manage dependencies carefully to avoid unnecessary executions or infinite loops.

---

## 4️⃣ useMemo

> `useMemo` memoizes expensive calculations.
> I use it when derived values depend on props or state and recalculating them causes performance issues.

---

## 5️⃣ useCallback

> `useCallback` memoizes functions to prevent unnecessary re-creation.
> It’s especially useful when passing callbacks to memoized child components.

---

## 6️⃣ useRef

> `useRef` stores mutable values without triggering re-renders.
> I use it for DOM access or to persist values across renders like timers or previous state.

---

# 🔹 STATE & DATA FLOW

## 7️⃣ Controlled vs Uncontrolled Components

> Controlled components are driven by React state and give full control.
> Uncontrolled components rely on the DOM and are useful for simple or performance-critical cases.

---

## 8️⃣ Lifting State Up

> When multiple components need the same data, I lift state to the nearest common parent.
> This keeps data flow predictable and avoids duplicate state.

---

## 9️⃣ Component Reusability

> I design components to be small, composable, and prop-driven.
> Business logic is extracted into hooks so UI components stay reusable.

---

# 🔹 ROUTING

## 🔟 React Router Basics

> I use React Router to handle client-side navigation.
> Routes are structured by feature, and protected routes are wrapped with auth guards.

---

# 🔹 PERFORMANCE OPTIMIZATION

## 1️⃣ Why use useCallback?

> To prevent unnecessary re-renders when passing functions to child components.
> This is important in complex UIs with memoized components.

---

## 2️⃣ How do you avoid unnecessary re-renders?

> By memoizing components, using `useMemo` and `useCallback`, and keeping state minimal.
> I also avoid storing derived data in state.

---

## 3️⃣ How do you structure a large React app?

> I use a feature-based folder structure.
> Each feature contains its components, hooks, services, and types.

---

## 4️⃣ How do you manage complex state?

> Local state stays in components, shared state goes into context or a store.
> I keep logic predictable and avoid global state unless it’s truly shared.

---

