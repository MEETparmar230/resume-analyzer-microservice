
from app.db import supabase

jobs = [
    {"title": "mern_developer", "skills": ["React","Node.js","MongoDB","Express","Redux","JWT"]},
    {"title": "java_developer", "skills": ["Java","Spring Boot","Hibernate","MySQL","REST API","JUnit"]},
    {"title": "python_developer", "skills": ["Python","Django","Flask","SQLAlchemy","REST API","Pandas"]},
    {"title": "data_scientist", "skills": ["Python","Pandas","NumPy","Scikit-learn","TensorFlow","NLP"]},
    {"title": "devops_engineer", "skills": ["Docker","Kubernetes","CI/CD","AWS","Terraform","Linux"]},
    {"title": "frontend_developer", "skills": ["HTML","CSS","JavaScript","React","Vue.js","SASS"]},
    {"title": "backend_developer", "skills": ["Node.js","Express","Python","Django","Java","REST API"]},
    {"title": "fullstack_developer", "skills": ["JavaScript","React","Node.js","MongoDB","Express","Redux"]},
    {"title": "aws_engineer", "skills": ["AWS EC2","S3","Lambda","CloudFormation","CloudWatch","IAM"]},
    {"title": "azure_engineer", "skills": ["Azure Functions","Azure DevOps","VMs","Cosmos DB","Active Directory"]},
    {"title": "gcp_engineer", "skills": ["Compute Engine","App Engine","Cloud Functions","BigQuery","Cloud Storage"]},
    {"title": "android_developer", "skills": ["Kotlin","Java","Android SDK","Jetpack","Room","Retrofit"]},
    {"title": "ios_developer", "skills": ["Swift","Objective-C","Xcode","CocoaPods","UIKit","Core Data"]},
    {"title": "machine_learning_engineer", "skills": ["Python","TensorFlow","PyTorch","Scikit-learn","Pandas","NumPy"]},
    {"title": "ai_engineer", "skills": ["Python","TensorFlow","PyTorch","Deep Learning","NLP","Computer Vision"]},
    {"title": "qa_engineer", "skills": ["Selenium","JUnit","Cypress","TestNG","Postman","JIRA"]},
    {"title": "security_engineer", "skills": ["Penetration Testing","Firewalls","Wireshark","Linux","AWS Security","OWASP"]},
    {"title": "data_engineer", "skills": ["Python","SQL","ETL","Airflow","Spark","Hadoop"]},
    {"title": "cloud_architect", "skills": ["AWS","Azure","GCP","Terraform","Kubernetes","Docker"]},
    {"title": "network_engineer", "skills": ["TCP/IP","Routing","Switching","Firewalls","Cisco","Juniper"]},
    {"title": "system_admin", "skills": ["Linux","Windows Server","Shell Scripting","Active Directory","VMware","Networking"]},
    {"title": "blockchain_developer", "skills": ["Solidity","Ethereum","Smart Contracts","Web3.js","Truffle","Ganache"]},
    {"title": "react_native_developer", "skills": ["React Native","JavaScript","Redux","Expo","iOS","Android"]},
    {"title": "flutter_developer", "skills": ["Flutter","Dart","Firebase","REST API","Provider","Bloc"]},
    {"title": "sql_developer", "skills": ["SQL","PL/SQL","MySQL","PostgreSQL","T-SQL","Oracle"]},
    {"title": "big_data_engineer", "skills": ["Hadoop","Spark","Kafka","Python","Hive","HBase"]},
    {"title": "business_analyst", "skills": ["Excel","SQL","Power BI","Tableau","Data Analysis","UML"]},
    {"title": "product_manager", "skills": ["Roadmaps","JIRA","Confluence","Agile","Scrum","Communication"]},
    {"title": "ux_ui_designer", "skills": ["Figma","Sketch","Adobe XD","Wireframing","Prototyping","Usability Testing"]},
    {"title": "game_developer", "skills": ["Unity","C#","Unreal Engine","3D Modeling","Animation","Physics"]},
    {"title": "embedded_systems_engineer", "skills": ["C","C++","Microcontrollers","RTOS","Embedded Linux","Debugging"]},
    {"title": "iot_engineer", "skills": ["Sensors","Arduino","Raspberry Pi","MQTT","Python","C++"]},
    {"title": "ruby_on_rails_developer", "skills": ["Ruby","Rails","PostgreSQL","RSpec","Git","HTML/CSS"]},
    {"title": "php_developer", "skills": ["PHP","Laravel","MySQL","Composer","REST API","JavaScript"]},
    {"title": "angular_developer", "skills": ["Angular","TypeScript","RxJS","NgRx","HTML","CSS"]},
    {"title": "vuejs_developer", "skills": ["Vue.js","Vuex","JavaScript","HTML","CSS","Axios"]},
    {"title": "csharp_developer", "skills": ["C#","ASP.NET","Entity Framework","SQL Server","REST API","MVC"]},
    {"title": "golang_developer", "skills": ["Go","Gin","Gorm","Docker","REST API","Kubernetes"]},
    {"title": "rust_developer", "skills": ["Rust","Actix","Tokio","Serde","Rocket","Cargo"]},
    {"title": "scala_developer", "skills": ["Scala","Akka","Spark","SBT","Functional Programming","Kafka"]},
    {"title": "kotlin_developer", "skills": ["Kotlin","Spring Boot","Android","Coroutines","Ktor","SQL"]},
    {"title": "tensorflow_developer", "skills": ["TensorFlow","Keras","Python","Numpy","Pandas","Deep Learning"]},
    {"title": "pytorch_developer", "skills": ["PyTorch","Python","TensorFlow","NumPy","Pandas","Deep Learning"]},
    {"title": "qa_automation_engineer", "skills": ["Selenium","Cypress","TestNG","JUnit","Python","Java"]},
    {"title": "seo_specialist", "skills": ["SEO","Google Analytics","Keyword Research","Backlinks","Content Marketing","On-Page SEO"]},
    {"title": "digital_marketing_specialist", "skills": ["Google Ads","Facebook Ads","SEO","Email Marketing","Analytics","Content Marketing"]},
    {"title": "salesforce_developer", "skills": ["Salesforce","Apex","Visualforce","Lightning","SOQL","Triggers"]},
    {"title": "sap_consultant", "skills": ["SAP","ABAP","FICO","MM","SD","HANA"]},
    {"title": "power_bi_developer", "skills": ["Power BI","DAX","SQL","Data Modeling","Excel","ETL"]},
    {"title": "tableau_developer", "skills": ["Tableau","SQL","Data Visualization","Calculations","Dashboards","Analytics"]},
    {"title": "linux_engineer", "skills": ["Linux","Shell Scripting","Networking","Bash","Python","Security"]},
    {"title": "ethical_hacker", "skills": ["Penetration Testing","Kali Linux","Metasploit","Wireshark","Python","Exploitation"]},
    {"title": "game_designer", "skills": ["Unity","C#","Blender","3D Modeling","Animation","UI/UX"]},
    {"title": "devops_consultant", "skills": ["Docker","Kubernetes","CI/CD","Terraform","AWS","Monitoring"]},
    {"title": "cloud_consultant", "skills": ["AWS","Azure","GCP","CloudFormation","Kubernetes","Docker"]}
]

# Insert into Supabase
for job in jobs:
    supabase.table("jobs").insert(job).execute()


print("Database initialization complete.")
