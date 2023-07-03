# FastAPI Dataset Publishing Application

This repository contains the source code for a FastAPI application designed to publish datasets in a way that adheres to the best practices laid out by ESIP, DCAT, and schema.org. The goal of this project is to enable the FAIR (Findable, Accessible, Interoperable, and Reusable) data principles. 

The application is built with Linked Data principles in mind and is designed to be consumed by various clients, including lower level models (LLMs) like ChatGPT, web applications, and human users.

## Features

- Basic FastAPI application following REST best practices
- JSON-LD serialization of JSON responses
- Caching of the JSON-LD context document
- Implementation of content negotiation according to DCAT guidelines
- Human-readable landing pages for each dataset in HTML format with embedded schema.org annotations
- Adherence to ESIP science on schema.org best practices for datasets
- Downloadable datasets
- Test-Driven Development approach with pytest
- Development in a devcontainer using Visual Studio Code with GitHub Copilot as an assistant
- Data validation using standardized vocabularies, potentially with tools like pySHACL
- Inclusion of persistent identifiers like ORCID and ROR in the dataset metadata
- OpenAPI API specification and .wellknown plugin-ai.json for LLM baesd co-pilots to consume the API.

## Getting Started

To get started with this project, clone the repository and set up the devcontainer in Visual Studio Code. Detailed instructions for each task are provided in the project instructions. 

## Co-Pilots Instruction Prompt
"I'd like to build a simple FastAPI application for publishing datasets. The application should adhere to best practices laid out by ESIP, DCAT, and schema.org, with an ultimate goal of enabling FAIR (Findable, Accessible, Interoperable, and Reusable) data principles.

The application should embody Linked Data principles and be designed with multiple types of consumers in mind, including but not limited to lower level models (LLMs) like ChatGPT, web applications, and human users.

The instructions are divided into the following tasks:

**Task 1: Setting up the FastAPI application**

Set up a basic FastAPI application following the REST best practices outlined at [this URL](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design). The final output should be a FastAPI application with a single route that returns a 'Hello, World!' message.

**Task 2: Implementing JSON-LD serialization**

The JSON responses from the application should use JSON-LD to semantically annotate the data, following the best practices at [this URL](https://w3c.github.io/json-ld-bp/). The JSON-LD should adhere to the schema.org vocabularies. The vocabularies should be published in a `context.jsonld` as per the JSON-LD best practices, adhering to FAIR best practices for vocabularies and ontologies.

**Task 3: Implementing content negotiation**

The application should implement content negotiation according to the DCAT guidelines, available at [this URL](https://www.w3.org/TR/dx-prof-conneg/). This content negotiation should support different representations of the dataset metadata, such as JSON-LD and text/turtle.

**Task 4: Implementing a '.well-known' route**

The application should implement a '.well-known' route that provides an 'ai-plugin.json' file and OpenAPI documentation.

**Task 5: Adhering to ESIP best practices for datasets**

The datasets should adhere to the ESIP science on schema.org best practices for datasets, available at [this URL](https://raw.githubusercontent.com/ESIPFed/science-on-schema.org/master/guides/Dataset.md). Specifically, each dataset should have a human-readable landing page with embedded schema.org metadata for dataset discovery. The landing page should be in HTML format.

**Task 6: Making the datasets downloadable**

The datasets should be downloadable through the application, with the format of the dataset specified in the metadata.

**Task 7: Implementing Test-Driven Development**

The application should be developed using a test-driven approach, with pytest as the testing framework.

**Task 8: Setting up the devcontainer and GitHub Copilot**

The application should be developed in a devcontainer using Visual Studio Code, and I'd like to use GitHub Copilot as an assistant for the development.

**Task 9: Validating the data**

The application should validate the data using standardized vocabularies wherever possible, potentially using tools like pySHACL for validation.

**Task 10: Including persistent identifiers in the dataset metadata**

The dataset metadata should include persistent identifiers such as ORCID and ROR for contributors, organizations, and other entities as applicable.

The goal is for a novice programmer to be able to build a semantically enhanced application using GitHub Copilot chat as an assistant. The application should serve as an example for FAIR data publication using the aforementioned best practices."

**Task 11: Implementing caching for the JSON-LD context**

The JSON-LD context document (`context.jsonld`) should be cached as per the W3C JSON-LD best practices. This will improve performance by reducing the need for repeated network requests. Use the `Cache-Control` HTTP header to control the caching behavior of the context document. For example, you can use `Cache-Control: public, max-age=86400` to indicate that the response can be cached by any cache, and that the maximum amount of time that the resource is considered fresh is one day (86400 seconds).

**Task 12: Implementing HTML landing pages for datasets**

Each dataset should have a landing page that can be accessed in HTML format. These pages should provide human-readable metadata about the dataset, and should include schema.org annotations embedded in the HTML to enhance discoverability. The application should be able to deliver these landing pages in response to HTTP requests that accept `text/html`, in accordance with the DCAT content negotiation by profile best practices.


## Contributing

Contributions are welcome! Please read the project instructions carefully and adhere to the given guidelines and best practices.

## License

[MIT](https://choosealicense.com/licenses/mit/)
