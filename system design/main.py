# 	1. You have 100 requests/second of location info(Like latitude and longitude) coming from your application user. You have to hit the external GPS service providers like google to get the address of that request. But the 3rd party providers have rate limiting of 10 requests/second. So they can only service 10 requests per second, More that that, they will reject the requests.
# 	How do you design the systems so that the number of requests in your system queue wont build up and slows down your system?
	
# 	Solution: 
# 	A) Below are few things that we can discuss with interviewer and try to understand which one is applicable for this usecase and try to design based on interviewer input
# 		1. Caching can help if request for same lattitude / longitude is coming
# 		2. does third party provider allow Array of lat / long in one request - if yes then that can help us. we can send multiple lat / lan in one request. it will degrade latency of system; however this is one possible way to do.
# 		3. do we have any priority of coming request ? serve only premium request and reject free / less priority request if we are not able to fulfill in certain period of time
	
# 	B)  Below is my approach,
# 		1. First check whether the request which hitting to the external API is having any pattern or unique id tagged to the lat/long co-ordinates.
# 		2. Maintain the cache for the request id to the result, and set the TTL. Not to overflow the cache servers.
# 		3. If we dont have the data for the request, then put the data into the pool, and implement the rate limiting at the client side, like token bucket + leaky bucket, or reslience4J.
# 		4. Once you get the data, record in the cache.
# 		5. If there are heavy requests in the pool, but set an API endpoint response to retry and send back to the customer (Atleast customer is aware of progress).
# 		6. return back the location info.
# 	Note: If you have a high demand of requests and you have very less req/sec then you have request external vendor to allow more traffic. Its all depends on the SLA and contract.
# 	If all you app request to external API is unique and there is no relation/pattern to establish then, I believe you dont have much options to optimise it. Either way you have spend the cost of increase the RPS or scarifice the customer experience.
# 	I'm open to suggestions/corrections/Imporovements.
	
# 	C) Centralised distributed Caching: you can develop a predictive model to decide TTL of cache. Ensure no duplicate calls to downstream service. This might not happen at 100 RPS but if the scale is higher there can be duplicate requests to downstream service. Clean the request before looking in the cache. Implement graceful handling of downstream service rejecting requests.
	
# 	D) If we have one instance of service consuming the lat/long at 100 req/s and hitting 3rd party API having a rate limit of 10 req/s, then we are looking at having a backlog of 90 req/s which will keep on growing. No matter what queuing strategy we use, the backlog will keep on increasing.
# 	One Naive solution is to put these lat/long requests in a queue and spinoff consumers which will pull the request from the queue and hit the 3rd party API.
# 	For this particular example, we can have 11 consumers(10+1 backup) consume events from the queue and hit the 3rd party API to get the address.
	
	
# 	2. I've been practicing for System design interviews for a while but I have trouble calculating the approximate number of servers that my system would use and I can't find a resource that shows how to calculate an approximate of servers.
# 	I know it depends a lot on the kind of design you're making, but anyone knows how to make a general estimation on servers?
	
# 	Solution:
# 		Facebook is not looking for those details. You have to understand the reason why you need to do capacity estimates. You need to determine the following
# 			1. The reads per second and the peak reads per second (when there is a spike). Tip: Just assume a peak of 5X or 10X the average reads per second.
# 			2. The writes per second and peak writes per second Same tip: peak writes per second is 5 or 10X average writes per second.
# 			3. Determine if your system is read heavy or write heavy.
# 			4. Roughly how much data you're going to have to store.
# 		From this information, you then need to infer important aspects of your design. For example, what latency do you need (ans low latency)? What type of databases do you need? Do you need relational or non relational? If you need NOSQL do you need a database that has master nodes or is masterless. etc...
# 		The purpose is to show that based on certain capacities, these are the reasons why you are choosing Technologies A, B and C.
# 		For example, if the system design is to 'Design Hacker Rank' used by 100K people for a weekly coding contest. 10 questions per contest.
# 		You will then determine how much data people will generate, and how much data you will need to store, the transactions per second. and peak TPS ie the capacity estimation. Then you will pick your database based on your estimates. Now here is the thing, you can choose EITHER SQL or NOSQL in this example. But you will have to JUSTIFY your choice. You justify based on your capacity estimates. In this example, if you start saying without justification that you want a NOSQL database, then that's wrong because you have not justified why NOSQL vs SQL.
# 		The point is not to do math. The point is to use the calculations to JUSTIFY the choices you are making in your system design.
# 		Let me repeat. The point is to only do enough calculations to justify your choices of database, storage, latency, CAP theorem etc...
# 		And the big tip is that you want to do these calculations quickly so that you can justify the choices you're making so that you can talk more about the individual components and the technologies you've chosen. No one cares about the exact number of servers.
		
# 		You want to determine if you need low latency or the system can accept high latency (it's async). Your capacity estimates are to determine what type of latency is acceptable. For example, if it's read heavy, real-time, you want low latency. You will also want to introduce distributed caching so the latency is reduced. In fact, in most system designs you will use your capacity estimates to say you need a low latency system for the best user experience. However, there can be systems where you don't need low latency. For example, if the system design question is to write a system to transcode videos offline for Netflix, then low latency is not really required because the system will be asynchronous in nature.
		
		
# 	3. You have to design a scalable multi player Ludo game. Game could be paused/resume.
# 	If a player is disconnected for some reason, when connected again she should be able to resume the game:
# 	Solution: ??
	
	
# 	4. I was asked the following question:
# 	Design a monitoring system that exposes an "Increment(<metric_name>)" endpoint that any other service can use to increment some metric such as "failed_sign_in". A live dashboard should display these metrics in 1 hour granularity, to be used for monitoring unusual behaviour (e.g. if the failed_sign_in metric increases a lot, it might mean the service is being abused).
# 	Solution: ??
	
# 	5. A coupon management system stores a definition of a coupon and also every time a user redeems a coupon. A coupon consists of an id, a title, a start date, end date, maximum number of coupons per user and also a maximum number of coupons across all users. When a user redeems a coupon the system keeps track of the users identifier, the datetime when the redemption occurred and a unique code that is generated by the application.
# 	The coupon management system is required to provide the following capabilities:
# 		• Provide an active list of coupons.
# 		• Determine if a consumer can redeem a coupons.
# 		• Store redemptions as they occur.
# 		• Provide reporting on the redemptions for a specific offer.
# 	The coupon management system is expected to have the following capacity:
# 		• Coupons up to 50000 unique coupons. Generally 100-500 active at any point in time.
# 		• Redemptions – Upwards of 1 billion rows. Expect at least 1 million redemptions per day.
# 	Requirements:
# 		1. Create a data model to represent the data in the above scenario. You are free to choose any storage mechanism you feel appropriate. The model should take into account the volume and expected operations into account.
# 		2. Define additional optimizations that you would apply to the basic data model. (For example if you were to choose SQL you might want indexes on certain columns) Note: Implementation/Code is not required.
		
# 	Solution:
# 	For the given requirements, we could leverage Cosmos DB in Azure as a backend datastore for the Coupon management system. Key motivation for selecting Cosmos DB is the considerable price savings in comparison to a SQL cluster, while at the same time providing for a scalable and highly available data storage environment.
# 	We will have a database that is configured for multi-region read-write to ensure high availablity. By default Cosmos DB indexes all fields in a document. We will define a custom indexing policy to only index the fields that we are interested in. This will lower the amount of storage used and improve the latency with writes.
# 	Entities
# 	In addition to the below mentioned fields, each entity will also define a partition key. The different entity sections will define how the partition key is created.
# 	CouponDefinition
# 	To store the different coupons and its related properties.
# 	Field Name Type Notes
# 	CouponDefinitionId Guid This will be the id field of the document to enforce unique constraints. It is called CouponDefinitionId here to make it very explicit and for easier reference from other entity sections.
# 	Title String 
# 	StartDate Date 
# 	EndDate Date Will have an index against this field to support the list of active coupons query.
# 	MaximumNumberOfCouponsPerUser Integer 
# 	MaximumNumberOfCoupons Integer 
# 	Partition key will be the string constant "CouponDefinition" across all records for this entity type.
# 	CouponRedemption
# 	Used to record a coupon redemption.
# 	Field Name Type Notes
# 	CouponRedemptionId Guid Unique id generated by the application when a coupon is redeemed. Will map to the id field of the document to enforce unique constraints.
# 	RedemptionDate DateTime 
# 	CouponDefinitionId Guid This will be the partionkey for this document type.
# 	UserId Guid 
# 	UserCouponRedemption
# 	Used to keep a count of redemptions made by each user.
# 	Field Name Type Notes
# 	CouponDefinitionId Guid This will be the partionkey for this document type. The value will be prefixed with the string "UserCouponRedemption".
# 	UserId Guid This will be the id field for the document to ensure unique constraints.
# 	RedemptionCount Integer Total number of redemptions made by the user for the coupon identified by the CouponDefinitionId field.
# 	Queries
# 		1. Provide a list of active coupons
# This can be retrieved by querying for CouponDefinition records with a filter on the EndDate.
# 		2. Determine if a customer can redeem a coupon
# The assumption here is that there are two requirements to be met before a user can redeem a coupon:
# 	Total number of coupon redemptions is less than or equal to MaximumNumberOfCoupons field in the coupon definition.
# 	Total number of coupon redemptions for a user is less than or equal to MaximumNumberOfCouponsPerUser field in the coupon definition.
# 	Solutions for requirment 1 are discussed further below. To meet requirement 2, we maintain a UserCouponRedemption record for each user, coupon combination. When a request is made to redeem a coupon:
# 	We first check this record to determine the number of existing redemptions by a user.
# 	We then proceed to increment and update the redemption count for the user.
# 	Cosmos DB provides an etag field for every document which can be used for optimistic concurrency checks when updating the redemption count.
# 	Requirement 2 requires us to keep an exact count of the number of redemption per coupon. This is a hard problem in a high volume distributed environment. Few solutions are proposed below:
# 		1. Not enforcing a strict count on the total redemptions per coupon
# In this model we keep an in memory count of the number or redemptions made for an active coupon.
# This list is periodically updated by a background task. We can leverage the change feed feature of Cosmos DB to calculate this count.
# A request to redeem a coupon will be checked against this in-memory count before proceeding further.
# The disadvantage with this approach is that we could potentially over redeem a coupon during a small window, but may be an acceptable compromise by the business.
# 		2. Pregenerate a list of CouponRedemption entries for a coupon
# In this model, the coupon redemptions entries for a coupon are pre-populated.
# The CouponRedemptionId and RedemptionDate fields for the record will be empty initially.
# When redeeming a coupon, we fetch a record with an empty CouponRedemptionId and update the CouponRedemptionId and RedemptionDate fields accordingly.
# CouponRedemptionId field will be indexed to make this query efficient.
# If the system is used alongside a shopping cart, where a redemption involves first adding the coupon to the cart and then redeeming it as part of payment, a separate field could be added to track this Reserved status which will then be updated to Confirmed.
# Key considerations: The above model ensures that we dont over redeem coupons. The requirement to pre-populate CouponRedemption entries has some implications which should be considered.
# Upfront cost of provisioning these records. This may mean that we will have to run with a higher RU allocation than would be otherwise required. However if we operate in a model where the Coupons are created in advance before it goes on sale, this pre-generation could be scheduled to a non-busy period for the system.
# A coupon may not be used to its full capacity, this would result in a lot of empty records and increased space consumption. We could provision these records with a Time To Live (TTL) setting that is set to expire when the coupon expires, or alternatively we could have a clean up job to remove the unused entries.
# 		3. Adopt a single writer approach
# The key issue we are facing here is that it is hard to keep an accurate count when there are concurrent writes.
# If we serialize these writes, then a single writer could keep track of the coupon redemption count.
# The challenge is that this approach wont scale in high workload environment.
# One approach is to shard the number of redemptions for a coupon across multiple nodes. Say for eg: a coupon has 1000 redemptions, then Node A can do upto 500 redemptions and Node B does the rest.
# We will require a smart router fronting these nodes, that can route the request based on the Coupon.
# Key considerations:
# This approach has the best of both worlds - preventing over redemptions and keeping the Cosmos DB cost minimal.
# However this comes with increased operational and development overhead.
# We can tweak and adopt these approaches to best fit the business model. If we can allow for some amount of over-redemptions then option 1 is preferred, followed by options 2 and 3.
# 		4. Store redemptions as they occur
# Every redemption will create a CouponRedemption record after populating the required fields.
# 		5. Provide reporting on the redemptions for a specific offer
# While a typical SQL model will allow for adhoc reports after the schema has been defined, the desired query patterns needs to be thought upfront with a NoSQL design. Some assumptions made here:
# 	We need to report on the total redemptions for a coupon
# 	The redemptions made should be reported per week or day or another unit of time as desired.
# 	For one of the above queries, we need to keep track of the total redemption count per coupon. The Change feed feature in Cosmos DB helps us to keep a running total of this count. We could persist this information for the desired time frame , as a new entity type to help with reporting. A background process can periodically consume these new record types and create a tailor fit materialised view for the report.
	
	
	
# 	6. KV store should be running as (at least) 2 different processes that replicate data between them (ie) we should be able to put in a Key and Value to Process 1 and query for the same Key on Process 2, for which we should get the corresponding Value.
# 	Using a common backend to processes / using an existing open source KV stores like redis, etc is not allowed
# 	Your solution should work even when we run two (or more) processes on multiple machines / containers connected over a network.
# 	We would like you to expose the store via a HTTP service that would allow us to GET / SET
# 	key-value pairs.
# 	$ curl -H "Content-type: application/json" -XPOST http://localhost:4455/set/key -d ‘“value”’
# 	OK
# 	$ curl -H “Accept: application/json” http://localhost:4466/get/key
# 	“value”
# 	Solution :
# 	It is a in memory key-value store using hashmap internally. In the implementation , I developed a jar which takes a configuration file that has the information about the peers end points, replication factor, port number to open etc., Once the process starts it starts serving the requests over HTTP endpoint. All the incoming put requests will be written to log structure(appended to list along with timestamp), this is used to replicated the data to peers, every put request ensures that key is written to replication factor number of peers. And the separate replicator thread runs in the process to replicate this log to all the peers excluding replicas along with the check pointing to be in sync with peers. If the get request is made to any peer and key is not available in that process, it will request the peer process for the key and updates the value locally and returns that to client. If the key is already available , it returns directly the value. In this case if the same key is updated in other peer and replication snapshot is not done yet, this will result in incorrect return value(limitation). Whenever the process goes down and comes back, it will not have any data and request for any old keys will result in requests to peers.
# 	Excuse me if I am not clear with explanation as it is my first post here, i will answer/edit the post on further questions/suggestions.
# 	Git link : https://github.com/BalaMahesh/simple-kv-store/tree/master
# 	Some how, my design is not accepted. I want to hear from you on the possible reasons. Thank you.
	
	
	
	
	
	
		
	
	
	
	
		
