# Querying a dataset with Hadoop and Hive

*Graduate course project (MSc, Computer Engineering, data analysis and big data, 2022-2023). Individual lab exercise on a sample dataset. The figures are illustrative.*

## Goal

Show the full path of a small big-data workflow: put a dataset into distributed storage, define a table over it, and answer business-style questions with SQL.

## Environment

- A virtual machine running a Hadoop distribution (Cloudera QuickStart), hosted in VirtualBox.
- HDFS for storage, Hive for the table layer, and the Hue web interface for queries.

## Data

A public Kaggle dataset, adapted for the scenario: internet users by region, gender and birth year. Values were edited for the exercise, so the counts do not reflect real populations.

## Steps

1. Prepare the dataset locally and copy it into HDFS.
2. Check the files in the HDFS browser and set access for the lab environment.
3. In Hue, create a Hive database and a table over the file.
4. Query the table: users by region, gender and birth-year range.
5. Compare regions and write the findings.

## Example questions answered

| Question | Result in the sample data |
|---|---|
| Female users born 1947 to 2007 in Europe | 150 |
| Male users born 1947 to 2007 in Europe | 160 |
| All users in Europe in that range | 310 |
| All users in the Middle East in that range | 78 |

## Real-world use

The same pattern supports audience analysis for digital advertising: counting users in a region, age band and segment before choosing where to show an advertisement.

## What I learned

- The difference between storing files (HDFS) and querying them as tables (Hive).
- Writing clear SQL for questions that start as business sentences.
- In a production setting the same workflow would use least-privilege access, a managed cluster and governed data; the lab shortcuts are for learning only.

## Limits

This is a teaching exercise on a small, edited dataset. It is not evidence of running a production data platform.
