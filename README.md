# Xtract Submission Template

Creating an metadata extractor with Xtract compability is easy. There are only
a few requirements and guiding principles.

## What is an Extractor?

An extractor, by definition, is simply the union of a function that inputs a 
file group and outputs a single metadata document and a virtual environment
with a collection of dependencies.



## Guiding principles

1. Relevant - extractors should generate metadata that enable an end-user to
accomplish a given task. The included information for an extractor is the union 
of necessary metadata for an extractor’s stakeholders.

2. Correct - extractors should guarantee metadata correctness. Ideally, extractors
should be validated via unit-testing. In the event that this is not possible
(the extractor is fully automated or executes at large scale), expert validation
is an acceptable alternative. Especially in domains of computer vision or machine
learning, "good enough" performance is acceptable.

3. Lightweight - extractors should be optimized for time and bandwidth to avoid
wasting computing resources.

4. Flexible - extractors should parse a type of file, rather than a specific 
schema (informally a file extension). Two methods to achieve this include 
code adaptation (changing the extractor) and schema conversion (changing 
the input).

5. Modular - extractors should extract only one type of data. When a data format
is present across multiple file types, say in the event of free-text describing 
an experiment and tabular experiment results, two separate extractors should be
used.

It is important to note that these principles are mainly guidelines: it is up to 
users to determine the degree to which these should be upheld. User needs will
vary, and therefore the guidelines may evolve to meet the needs of users across 
different domains.

# Steps

## Step 1 - Clone this repository
Xtract Submission Template provides a starting point for users interested in 
creating an extractor.

## Step 2 - Populate extractor skeleton
Xtract provides the code skeleton `extractor.py` along with a Dockerfile and 
requirements file. These files are pre-populated with the minimum viable 
extractor. 

Each subcomponent should be independent and have no side-effects on the input,
as this prevents repeated IOs associated with reopening the file (P3) and allows 
the extractor to be expanded upon more easily over time (P5).

## Step 3 - Publish extractor using XCLI (WIP)
The Xtract CLI, abbreviated `xcli`, provides an convenient CLI to manage an 
Xtract deployment. One such feature is using `xcli`to upload an extractor.

