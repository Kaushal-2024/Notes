# TypeScript Crash Course – Key Notes & Reference

## Table of Contents
- [Dynamic Object Types](#dynamic-object-types)
- [Tuples](#tuples)
- [Intersections & Unions](#intersections--unions)
- [Types vs Interfaces](#types-vs-interfaces)
- [Enums vs Unions](#enums-vs-unions)
- [Type Narrowing](#type-narrowing)
- [Type Assertions](#type-assertions)
- [Classes & OOP](#classes--oop)
- [Utility Types](#utility-types)
- [Generics](#generics)
- [Advanced Types](#advanced-types)
- [TypeScript Project Setup](#typescript-project-setup)
- [Recommended Resources](#recommended-resources)

---

## Dynamic Object Types

- Use index signatures for dynamic keys:
  ```typescript
  type MyObj = { [key: string]: number | string | boolean }
  ```
- Prefer `Record<string, T>` for exhaustive keys.

---

## Tuples

- Tuples are ordered arrays with fixed types.
- Use `as const` for strict tuple types.
- Optional tuple elements must be last.
- Example:
  ```typescript
  type Ticket = [number, string, boolean?]
  ```
- You can use rest elements in tuples:
  ```typescript
  type Command = [string, ...string[]]
  ```

---

## Intersections & Unions

- **Intersection (`&`)**: Combines types, must satisfy all.
- **Union (`|`)**: Can be any of the listed types.
- Example:
  ```typescript
  type A = { id: number }
  type B = { name: string }
  type AB = A & B // { id: number, name: string }
  type Either = A | B
  ```

---

## Types vs Interfaces

- Prefer `type` for most cases.
- Use `interface` for declaration merging or extending global types.
- Both can be extended and mixed.
- `interface` supports declaration merging, `type` does not.

---

## Enums vs Unions

- Avoid enums; prefer union types.
- Enums add JS code, unions are erased at compile time.
- Example:
  ```typescript
  type CardSuit = 'hearts' | 'diamonds' | 'clubs' | 'spades'
  ```
- Enums can be reverse-mapped, but unions are simpler and safer.

---

## Type Narrowing

- Use `typeof`, `instanceof`, `in`, and custom type predicates.
- Example:
  ```typescript
  if (typeof value === 'string') { /* ... */ }
  if ('property' in obj) { /* ... */ }
  ```
- Discriminated unions are powerful for narrowing.

---

## Type Assertions

- Use `as` when you know the type better than TypeScript.
- Use non-null assertion (`!`) for values you know aren't null.
- Double assertion (`value as unknown as Type`) is risky and should be avoided.

---

## Classes & OOP

- Use `class` for OOP, with `private`, `protected`, and `public` members.
- Prefer `#private` for JS runtime privacy.
- `protected` allows access in subclasses.
- Abstract classes provide a template for subclasses.
- Use `implements` to enforce interface/type contracts.

---

## Utility Types

- `Partial<T>`: All properties optional.
- `Required<T>`: All properties required.
- `Readonly<T>`: All properties readonly.
- `Pick<T, K>`: Pick specific keys.
- `Omit<T, K>`: Omit specific keys.
- `Record<K, T>`: Object with keys K and values T.
- Example:
  ```typescript
  type User = { id: number, name: string }
  type UserInfo = Partial<User>
  ```

---

## Generics

- Use generics for reusable types/functions.
- Example:
  ```typescript
  function getFirst<T>(arr: T[]): T | undefined { return arr[0]; }
  ```
- You can constrain generics:
  ```typescript
  function pluckEmail<T extends { email: string }>(arr: T[]): string[] { ... }
  ```
- Generic types/interfaces/classes are powerful for abstraction.

---

## Advanced Types

- Conditional types:
  ```typescript
  type IsString<T> = T extends string ? true : false
  ```
- Mapped types:
  ```typescript
  type OptionalSoldier = { [K in keyof Soldier]?: Soldier[K] }
  ```
- Infer keyword for extracting types:
  ```typescript
  type ReturnType<T> = T extends (...args: any[]) => infer R ? R : never
  ```
- Use mapped + conditional types for advanced filtering.

---

## TypeScript Project Setup

- Use `tsconfig.json` for configuration.
- Prefer strict mode (`"strict": true`).
- Use Vite for bundling modern TS projects.
- Install TypeScript locally (`npm i -D typescript`).
- Use declaration files (`*.d.ts`) for global types or third-party JS libraries.
- Use `@ts-ignore` or `@ts-expect-error` for ignoring specific lines (use sparingly).

---

## Recommended Resources

- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
- [WebDevSimplified YouTube](https://www.youtube.com/c/WebDevSimplified)
- [Boot.dev Courses](https://boot.dev)

---

**Tip:** Use this doc as a quick reference and expand sections with your own examples and notes as you learn.

