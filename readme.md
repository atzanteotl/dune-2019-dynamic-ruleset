This is a dynamic ruleset for the 2019 Dune board game rendered as a html page. 
A live version is [available here](http://andrewc.me/dune/).

---

**Rules Guidelines**

- Rules must be written in active voice, with subject-verb-object wherever possible (e.g. "Players must announce how many cards..."")
- General rules should start with the noun "Players".
- Faction specific rules should start with the faction name.
- Indented rules are clarifications, constraints, or exceptions for the parent rule.
- Clarifications and constraints do not need to name the subject of the sentence.
- Optional rules use the word "may"; compulsory rules use "must".

---

**Building the ruleset**

The rules are generated from a CSV file (rules.csv) using a jinja2 template. Edit rules.csv and run process-rules.py to generate a new index.html.

The rules.csv has the following fields:

- **class1** - empty or "alliances". Used to identify alliance specific rules. They will appear as grey boxes in the ruleset when the alliance button is pressed.
- **class2** - empty, bene-rule, fremen-rule, atreides-rule, harkonnen-rule, spacing-rule, emperor-rule. Used to identify faction specific rules. There are advance, basic, and "no" variants of each class. (e.g. no-fremen-rule, fremen-advance-rule).
- **faction** - used to highlight a particular faction rule to indicate that this is a specific *rule for that faction*.
- **section** - where it appears in the rulset.
- **subsection** - which subsection (i.e. phase) it appears in the ruleset.
- **depth** - indent of the rule.
- **rule** - the text of that rule. Can be specified in basic markdown.

--- 

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.
