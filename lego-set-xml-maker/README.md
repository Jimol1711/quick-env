This program should is supposed to help me find specific pieces for specific lego sets I have which are missing those pieces. I want to use it to filter for specific sets. I will provide a set number, and the program should tell me which pieces that set is missing and show me a picture of the piece.

The first part should be done through and algorithm that works with an xml file taken from a Bricklink wanted list I created. This xml file is of lego pieces, and each piece has a remark. This remark includes every set that needs that piece in a format "<SET NUMBER>x<QUANTITY>" separated by commas. So for instance, if a piece is needed 3 times on set 41234 and 1 time in set 45645, the remark column will have this entry: "41234x3, 45645x1".

The format of the xml file is:

<INVENTORY>
<ITEM>
<ITEMTYPE>P</ITEMTYPE>
<ITEMID>87846</ITEMID>
<COLOR>7</COLOR>
<MAXPRICE>-1.0000</MAXPRICE>
<MINQTY>1</MINQTY>
<CONDITION>X</CONDITION>
<REMARKS>4526x1</REMARKS>
<NOTIFY>N</NOTIFY>
</ITEM>
...
</INVENTORY>

Where in ... go all other entries. Here the relevant parts are "ITEMID" and "REMARKS" 