The goal of the project is to manage trees in a certain environment (Scalable environment).
This includes the location, type and count of trees, this helps us to manage and plant
different species of trees.

CAP Theorem: Consistency,and Partition Tolerance should be considered in this project.

{<br />
&nbsp;&nbsp;&nbsp;&nbsp;  Name (Name of the area to be managed)<br />
 &nbsp;&nbsp;&nbsp;&nbsp;  Area (Area covered)<br />
&nbsp;&nbsp;&nbsp;&nbsp;   Treetype (List of tree types in the area)<br />
&nbsp;&nbsp;&nbsp;&nbsp;   \[<br />
 &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;    {<br />
 &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;      name (Tree name)<br />
 &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;      count (Tree count)<br />
 &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;    },<br />
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     {<br />
  &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;   &nbsp;&nbsp;&nbsp;&nbsp;   name (Tree name)<br />
  &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;   &nbsp;&nbsp;&nbsp;&nbsp;   count (Tree count)<br />
 &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;    }<br />
 &nbsp;&nbsp;&nbsp;&nbsp;  \]<br />
}<br />

Example:<br />
{<br />
 &nbsp;&nbsp;&nbsp;&nbsp;  “Name”: Garden<br />
 &nbsp;&nbsp;&nbsp;&nbsp;  “Area”: 600 sq.ft<br />
 &nbsp;&nbsp;&nbsp;&nbsp;  Treetypes : [{“name”: “Bamboo”, “count”: 10}, {“name”: “Pine”, “count”: 1}]<br />
}<br />


* Database: MongoDB
* Language: Python and Flask web Framework
* Frontend: HTML and CSS
