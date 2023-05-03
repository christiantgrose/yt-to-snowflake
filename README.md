<b>YouTube Data Engineering Project</b>

<p>This project involves scraping data from YouTube using a Python script and storing it in a JSON file. The JSON file is then loaded into an S3 bucket in AWS. The data is then transferred to Snowflake using an external stage to the S3 bucket.

The JSON data is then loaded into a table with a single VARIANT column. A view is created from this table to flatten and normalize the JSON data. Finally, the normalized data is used to create a new table.</p>

<b>Project Objective</b>

<p>The main objective of this project is to demonstrate the ability to extract data from a web source, store it in the cloud, and normalize it for use in data analytics.</p>

<b>Data Sources</b>

<p>The data source for this project is YouTube. The data is scraped using a Python script and stored in a JSON file.</p>

<b>Technologies Used</b>

<p>
The following technologies were used in this project:
<ul>
<li>Python</li>
<li>AWS S3</li>
<li>Snowflake</li>
</ul></p>

<b>Accomplishments</b>
<p>
The following accomplishments were achieved in this project:
<ul>
<li>Successfully scraped data from YouTube using a Python script</li>
<li>Loaded the data into an S3 bucket in AWS</li>
<li>Transferred the data to Snowflake using an external stage</li>
<li>Loaded the data into a table with a single VARIANT column</li>
<li>Created a view to flatten and normalize the JSON data</li>
<li>Created a new table with the normalized data</li>
</ul></p>

<b>Usage</b>

To run this project, you will need access to the following:

<ul>
<li>A YouTube API key</li>
<li>An S3 bucket in AWS</li>
<li>A Snowflake account</li>
</ul>

Once you have access to these resources, you can follow these steps:
<ul>
<li>Clone this repository to your local machine.</li>
<li>Open the Python script youtube_scraper.py and update the YouTube API key.</li>
<li>Run the Python script to scrape the data and store it in a JSON file.</li>
<li>Upload the JSON file to your S3 bucket in AWS.</li>
<li>Create an external stage in Snowflake to your S3 bucket.</li>
<li>Load the JSON data from the external stage into a table with a single VARIANT column.</li>
<li>Create a view to flatten and normalize the JSON data.</li>
<li>Create a new table with the normalized data.</li>
</ul>

<b>License</b>

This project is licensed under the MIT License. See the LICENSE file for details.

<b>Contact</b>

If you have any questions or feedback, please feel free to contact me at christiantgrose@gmail.com.
