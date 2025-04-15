---
### Illinois State Buildings Visualization
---

### The Data  
[Click here to view the dataset](https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/building_inventory.csv)

### The Analysis  
[Click here to view the Python Notebook](https://github.com/Olivialxy/Olivialxy.github.io/blob/main/HW5.ipynb)

---

### Plot 1: Total Square Footage by Agency

This bar chart shows the total square footage of state-owned buildings managed by each Illinois government agency. I made this plot to better understand how building space is distributed across different agencies — in other words, which departments are using the most physical infrastructure. I grouped the data by “Agency Name” and calculated the total square footage using pandas. This was a simple transformation but helped me get a clearer overview of the dataset. 

I used a horizontal bar chart because long agency names are easier to read this way. I encoded square footage on the x-axis and agency names on the y-axis. To highlight the differences, I applied a blue color scale, where darker shades show larger amounts of space. The color helps emphasize which agencies control the most space without needing to read exact values. I sorted the data so that the biggest agencies appear first — this makes it faster to scan and compare. I decided not to make this plot interactive since it's meant to give a high-level summary.

---

### Plot 2: Interactive Bar Chart by City and Building Usage Type

This chart breaks down the number of buildings in each city, organized by how those buildings are used — for example, as offices, educational facilities, storage, and more. I created this plot to explore how state-owned buildings are distributed across Illinois based on their purpose, and where different types of buildings are concentrated. I started by grouping the data using pandas by both “City” and “Usage Description” and counted the number of buildings for each pair. I also removed rows that didn’t have a usage category since they wouldn’t add much value to the chart.

I used a vertical bar chart here, with city names on the y-axis and the building counts on the x-axis. I colored each bar based on the city, which makes the chart more visually appealing and also easier to navigate when scanning different locations. To make the chart more flexible, I added a dropdown menu so users can pick one usage type at a time. When you select a category, like “Office” or “Education,” the chart updates to show which cities have buildings that match that use. This makes it easy to spot which cities focus more on certain building types, or compare usage across regions.

---

### About the Interactivity

The interactive feature in the second chart makes it much more useful for exploring the dataset. I used Altair’s `selection_single()` with a `binding_select` dropdown menu to let users filter the chart by building usage type. This keeps the chart from feeling overwhelming and helps viewers dig into specific parts of the data depending on their interests. Instead of seeing every city and every building use all at once (which would be messy), the dropdown gives people a simple way to isolate what they care about — like just looking at “Laboratory” or “Residential” buildings. I think this kind of interaction makes the chart more engaging and informative, especially for people trying to find patterns or differences between cities.
