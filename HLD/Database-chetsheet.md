# Cheatsheet for Databases in High Level System Design
A Cheat Sheet for identifying databases suitable for high-level system design.

---
## 1. Time series databases 

Great for storing data associated with timestamps.

Useful for storing data like stock prices, monitoring, IoT, and real-time data analytics.

Commonly used time series databases include InfluxDB, OpenTSDB, and Prometheus.

Have high write thourghput and offer high availability by clustering.

---
## 2. Graph-based databases

Can be extremely useful for handling relationships between entities.

Useful for Social-network application and network infrastructure.

Graph databases excel in managing different kinds of traversals, making them suitable for social networks and network infrastructure.

Examples of common graph-based databases are Neo4j and Amazon Neptune, both following ACID properties.

---
## 3. Cassandra 

Used for real-time analytics, monitoring, and IoT data.

Cassandra offers high throughput and availability due to clustering

Model your data to focus reads on primary keys and use Cassandra query language similar to SQL.

---
## 4. MongoDB

MongoDB's dynamic schema allows for flexible data structures.

Documents within a collection can have different fields without affecting others.

Suitable for use cases with evolving data requirements like catalogues and product inventories.

---
## 5. Dynamo DB

Dynamo DB is managed by AWS for varying workloads.

Dynamo DB is reliable for seamless performance in gaming, web apps, and mobile apps.

Dynamo DB supports flexible schema but requires determining the primary key structure in advance

---
## 6. Relational databases 

Have fixed structure and asset compliance, but horizontal scaling can be challenging.

Relational databases are great for transactional data in financial cases, but horizontal scaling can be tricky due to asset compliance.



MySQL, Mariya DB, Postgre SQL Example of realtional databases.

---
## 7. Hadoop

Hadoop is No-SQL database.

HBase is a NoSQL DB used for big data and integrates seamlessly with Hadoop ecosystem, making it suitable for use with HDFS, MapR, or Spark. 

## 8. Blob storage

Use for store data like images.

Amazone S3 is example of blob storage.

---

Understanding databases for high level system design

Consider various factors like cost, data security, and compliance when choosing databases for real scenarios

Also, consider community support, feature requirements, and integration for different programming languages and tools