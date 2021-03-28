---
substitutions:
    a: 100*2
    b: 2
    c: 100
---

Here is the variable: {{a}} and {{b}}. Interestingly, I think I can do simple math though:

- {{b}} x {{c}} = {{b*c}}
- {{b}} + {{c}} = {{b+c}}
- {{b}} / {{c}} = {{b / c}}

What I really want though, is to use a python function and then do a Jinja2 substitution:

```{code-block} python

def random_velocity():
    import random

    x = random.randint(0,100)
    v = random.randint(200,300)

    return x*v
```

The output of the python function is: {{random_velocity()}} m/s.