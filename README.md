# Xtract Submission Template

Creating an extractor with Xtract compability is easy -- there are only a few requirements.

## Requirements
- Must be compatible with both Docker and Singularity containers
- Extractor must run out of an air-gapped environment
- The function `execute_extrator` must serve as the entry point for the program in main
- As of 3/28/2022, `execute_extractor` may only operate on one file at a time.

In most cases it is fairly straightforward to write Xtract ports, but new extractors targetting wanting to take advantage of Xtract's ecosystem should be designed with these basic requirements in mind.

# Steps

## Step 1 - Clone this repository
Xtract Submission Template provides a starting point for users interested in creating an extractor.

## Step 2 - Populate extractor skeleton
Xtract provides the code skeleton `extractor.py` along with a Dockerfile and requirements file. These files are pre-populated with the minimum viable extractor. We recommend creating extractor components separately, and return a dictionary of function calls in the main method `extract_main`.

Look to `xtract-python` for a sense of extractor structure.

## Step 3 - Publish extractor using XCLI (WIP)
The Xtract CLI, abbreviated `xcli`, provides an convenient CLI to manage an Xtract deployment. One such feature is using `xcli`to upload an extractor.
