# Kubernetes Security Research Project

A hands-on Kubernetes security lab showing how common misconfigurations can be chained into a realistic attack, and how layered defenses stop it.

The project compares two versions of the same cluster:

* **Vulnerable configuration**: intentionally insecure setup used to demonstrate the attack path
* **Secure configuration**: hardened setup using Kubernetes security controls

## What I built

I created a local Kubernetes lab with two namespaces:

* `target-namespace`: contains a victim Flask API with fabricated customer data
* `attacker-namespace`: contains a simulated compromised internal dashboard

The vulnerable version shows how an attacker inside one pod can abuse weak Kubernetes configuration to discover resources, access the Kubernetes API, and retrieve sensitive data from another namespace.

The secure version fixes the attack path using defense-in-depth instead of relying on one single control.

## Main security topics

This project focuses on:

* **Namespace isolation**: showing that namespaces organize resources, but do not block network traffic by default
* **RBAC and service accounts**: showing how service account tokens can become dangerous when permissions are too broad
* **Secrets management**: replacing ConfigMaps with Kubernetes Secrets for sensitive data
* **Network Policies**: restricting cross-namespace communication
* **Pod Security Standards**: enforcing safer runtime settings for containers
* **Security contexts**: running containers as non-root and reducing privilege escalation options

## Attack path

The vulnerable setup demonstrates this chain:

```text
Compromised pod
→ service account token access
→ Kubernetes API enumeration
→ namespace and service discovery
→ ConfigMap discovery
→ sensitive data exposure
```

The important part is that the attack does not depend on one dramatic vulnerability. It works because several small misconfigurations support each other.

That is exactly why Kubernetes security needs layered controls.

## Defense-in-depth implementation

In the hardened version, I added:

* dedicated service accounts for each workload
* disabled automatic mounting of service account tokens
* Kubernetes Secrets instead of ConfigMaps for sensitive data
* default-deny Network Policies
* restricted Pod Security Standards on namespaces
* container security contexts with non-root execution, dropped capabilities, and privilege escalation disabled

## Tech stack

* Kubernetes / MicroK8s
* Docker
* Python Flask
* Kubernetes YAML manifests
* Network Policies
* RBAC / Service Accounts
* Pod Security Standards
* Linux container security contexts

## What this project demonstrates

This project shows that Kubernetes security is not about one perfect setting. A cluster becomes safer when multiple controls work together.

RBAC limits what a pod can do through the API.
Network Policies limit where it can connect.
Pod Security Standards limit what it can do at runtime.
Secrets management reduces accidental exposure of sensitive data.

The final result is a practical offensive and defensive Kubernetes lab that demonstrates how misconfigurations are exploited and how they can be mitigated properly.

## Disclaimer

This project is for educational purposes only. All customer data used in the lab is fabricated.
::: 
