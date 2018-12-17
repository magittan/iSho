# iSho
Front End that uses Big World Preprocessing module to display Kensho data.

### Inspiration

iSho aims to spark interest in the beauty of both the interconnectivity of global financial markets and in the field of data visualization. Using the Kensho API and the D3.js library, we wanted to visualize and transform multifaceted data about these markets by displaying connections within the same industry and connections across multiple industries..

### What it does

In a force graph, companies are represented as nodes which linked by industry, by size, or by customer-client or supplier-consumer relationship. These relationships are clearly visible in the graph, and each industry is highlighted to emphasize the cross-industry relationships.

The user interacts with the interface by mousing over and clicking on the various entities of the graph, which allows the user to view the number of connections for each entity. The user can also drag the entities in order to view the connections better.

### How we built it

We implemented a Kensho client from which we extracted information about equity relationships by calling the REST API. These requests were handled through the Kensho API Client using Python, stored as JSON objects, and visualized through D3.js as an interactive graph.

### Challenges we ran into

The API was throttled heavily in the middle of the night, which limited the amount of work we were able to do. Learning JavaScript was also new for some of us.

### Accomplishments that we're proud of

We created a polished JavaScript application and visualized the entire S&P 500.

### What we learned

In addition to honing our JavaScript and front-end web development skills, we also learned that perseverance is key.

### What's next for iSho

Extracting more information from the Kensho database, such as timelines related to each of the entities, will allow us to visualize other branches of Kesho’s knowledge graphs. We will extrapolate from these visualizations in order to make predictions about financial markets and to gain insights into relationships that are otherwise difficult to observe.
