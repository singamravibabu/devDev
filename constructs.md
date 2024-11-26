# Constructs are used to construct programs
## constructs: if, for, while, with, def, class, ...

### if construct / statement
- Conditional construct used in decision making
- Conditional branching construct
- After passing 10th standard:
    - MPC
    - BiPC
    - CEC
    - MEC
    - Polytechnic
    - Work

- Syntax:

if <bool_exp>:          # if clause; first clause (required); one clause
    block               # (intended) block: statement(s)

[elif <bool_exp>:       # elif clause; optional clause; zero to many clauses
    block]...           # block statements must be equally indented

[else:                  # else clause; optional clause; zero or one clause
    block]              # block is executed conditionaly, not for else clause

### loops: for & while
- loops are used to execute a block repeatedly
- 'for' is a collection (countable) loop
- 'while' is a conditional loop

### for loop (construct) - collection (countable)
- 'for' loop is a finite loop, which means we can't run 'for' loop indefinitely
- Syntax:
for <var> in <collection>:
    block