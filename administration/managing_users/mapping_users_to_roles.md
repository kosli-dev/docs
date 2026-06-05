---
title: Mapping users to roles
description: Recommended mappings from common organizational roles to Kosli roles.
---

When implementing Kosli, you need to map organizational roles to [Kosli roles](/administration/managing_users/roles_in_kosli). This table provides recommended mappings based on typical responsibilities:

| Organizational Role | Recommended Kosli Role | Alternative | Rationale |
|---------------------|------------------------|-------------|-----------|
| **Platform Engineers** | Member | Admin (for leads) | Platform engineers need to set up flows, manage service accounts, configure integrations, and implement Kosli across teams. Member role provides these capabilities. Lead platform engineers managing the overall setup may need Admin access. |
| **Application Developers** | Member | Reader (for view-only) | Developers typically need to report attestations and manage flows for their applications. Member role enables this. Some developers may only need visibility into deployments and compliance status, making Reader sufficient. |
| **Security & Compliance** | Admin | N/A | Security and compliance teams need to manage policies, review audit data, control user access, and configure organization-wide settings. Admin role is required for these governance responsibilities. |
| **Sponsors** | Reader | N/A | Sponsors need visibility into adoption progress, compliance status, and overall system health but don't need to make technical changes. Reader role provides necessary oversight without operational access. |

## Understanding the mapping

This mapping is a starting point. Your organization's structure and responsibilities may require adjustments:

- **Small teams**: Developers might need Admin access if they handle all aspects
- **Large enterprises**: Strict separation may require more Readers, fewer Admins
- **Regulated industries**: Security teams might need dedicated Admin accounts separate from operations

The key principle: Assign the minimum role required for someone to fulfill their responsibilities effectively.

## Learn more about organizational roles

For detailed guidance on each organizational role's responsibilities during Kosli implementation, see:

- [Implementation Guide: Roles and Responsibilities](/implementation_guide/phase_1/roles_and_responsibilities/overview)
- [Platform Engineers](/implementation_guide/phase_1/roles_and_responsibilities/platform_engineers)
- [Application Developers](/implementation_guide/phase_1/roles_and_responsibilities/app_developers)
- [Security & Compliance](/implementation_guide/phase_1/roles_and_responsibilities/security_compliance)
- [Sponsors](/implementation_guide/phase_1/roles_and_responsibilities/sponsors)
