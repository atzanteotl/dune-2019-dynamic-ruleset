This is a dynamic ruleset for the 2019 Dune board game rendered as a html page. 
A live version is [available here](http://andrewc.me/dune/).

---

**Building the ruleset**

The rules are generated from a CSV file (rules.csv) using a jinja2 template. Edit rules.csv and run process-rules.py to generate a new index.html.

The rules.csv has the following fields:

**class1** - empty or "alliances". Used to identify alliance specific rules. They will appear as grey boxes in the ruleset when the alliance button is pressed.

**class2** - empty, bene-rule, fremen-rule, atreides-rule, harkonnen-rule, spacing-rule, emperor-rule. Used to identify faction specific rules. There are advance, basic, and "no" variants of each class. (e.g. no-fremen-

**rule**, fremen-advance-rule).

**faction** - used to highlight a particular faction rule to indicate that this is a specific *rule for that faction*.

**section** - where it appears in the rulset.

**subsection** - which subsection (i.e. phase) it appears in the ruleset.

**depth** - indent of the rule.

**rule** - the text of that rule. Can be specified in basic markdown.
