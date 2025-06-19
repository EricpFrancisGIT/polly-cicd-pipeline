# 📢 Pixel Learning Co. – Serverless Audio Delivery Pipeline

A lightweight, serverless solution that automatically converts course content into audio using **Amazon Polly**, **S3**, and **GitHub Actions** — designed for accessibility, automation, and rapid deployment.

---

## 🚀 Overview

**Pixel Learning Co.** is a digital-first education startup focused on improving learning accessibility. This project converts text-based course content into audio format using **Amazon Polly**, stored in **Amazon S3**, and orchestrated by **GitHub Actions** to eliminate manual steps.

### 🎯 Objectives

- 🔁 **Automate Content Conversion**: Text updates in GitHub are automatically turned into audio files.
- 🧪 **Ensure Content Readiness**: Separate outputs for **beta** (PRs) and **production** (merges).
- 🦾 **Increase Accessibility**: Audio versions of all content for inclusive learning.
- 💰 **Minimize Overhead**: Fully serverless, low-maintenance, cost-effective solution.

---

## 🧠 Why Use Amazon Polly?

- ⚡ **Speed & Simplicity** – Instant speech synthesis with no ML training.
- 📈 **Scalability** – Handles traffic without provisioning or scaling effort.
- 🗣️ **Realistic Voices** – Neural voice support across multiple languages.
- 🧩 **Easy Integration** – Boto3-compatible, fits naturally in automation pipelines.

## 🤖 Why GitHub Actions?

- 🔄 **Automation-Ready** – Triggers on pull requests and merges.
- 🧪 **Environment Separation** – Differentiates between `beta` and `prod` audio outputs.
- 🧑‍💻 **Dev-Centric** – Resides in the dev workflow with GitHub-hosted source content.

---

## 📁 Repository Structure

```bash
.
├── .github/
│   └── workflows/
│       ├── on_pull_request.yml  # Creates beta.mp3 on PRs
│       └── on_merge.yml         # Creates prod.mp3 on merges
├── synthesize.py                # Python script to synthesize text to speech
├── speech.txt                   # Sample course content to convert
└── README.md

## SETUP aka "HOW TO USE THIS"

✅ Requirements
🧪 Foundational Features

    Text-to-Speech Functionality

        Create a speech.txt file with sample content.

        Run synthesize.py to generate an .mp3 using Amazon Polly.

    S3 Upload Integration

        Upload the .mp3 file to a specified S3 bucket under the polly-audio/ prefix.

    CI/CD Automation with GitHub Actions

        on_pull_request.yml: Triggered on pull requests → uploads beta.mp3.

        on_merge.yml: Triggered on merges → uploads prod.mp3.

    Credential Management

        Store AWS credentials in GitHub Actions secrets:

            AWS_ACCESS_KEY_ID

            AWS_SECRET_ACCESS_KEY

            AWS_REGION

            S3_BUCKET_NAME

🔧 Setup Instructions

1. 🪣 AWS Configuration

    Create an S3 bucket (e.g., pixel-audio-bucket)

    Create an IAM user with the following permissions:

        polly:SynthesizeSpeech

        s3:PutObject

2. 🔐 GitHub Secrets

Go to Settings > Secrets > Actions and add:
Name	Description
AWS_ACCESS_KEY_ID	IAM user's access key
AWS_SECRET_ACCESS_KEY	IAM user's secret key
AWS_REGION	e.g., us-east-1
S3_BUCKET_NAME	Name of your S3 bucket

3. 📄 Modifying Text

    Edit the contents of speech.txt in your branch.

    Commit the change to trigger the PR or merge workflow.

4. 🔁 Triggering Workflows
Action	Trigger	Output
Pull Request	on_pull_request.yml	beta.mp3
Merge to main	on_merge.yml	prod.mp3
5. 🔍 Verifying Upload

    Navigate to your S3 bucket.

    Look for:

        polly-pixel-learning-s3/beta.mp3 (PRs)

        polly-pixel-learning-s3/prod.mp3 (Merges)

📬 Contact

Questions or feedback? Please open a ticket or contact me directly: eric.francis1103@gmail.com

Thank you!!
