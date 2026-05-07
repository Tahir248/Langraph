---
config:
  flowchart:
    curve: linear
---
graph TD;
        __start__([<p>__start__</p>]):::first
        node1(node1)
        node2(node2)
        __end__([<p>__end__</p>]):::last
        __start__ --> node1;
        node1 -. &nbsp;no&nbsp; .-> __end__;
        node1 -. &nbsp;yes&nbsp; .-> node2;
        node2 --> __end__;
        classDef default fill:#f2f0ff,line-height:1.2
        classDef first fill-opacity:0
        classDef last fill:#bfb6fc