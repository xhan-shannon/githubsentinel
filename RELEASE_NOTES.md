# Github Sentinel v0.1 Release Notes

## Introduction
This release introduces significant enhancements to the 'Github Sentinel' project, including support for GitHub API authentication and subscription management for multiple repositories.

## Key Features

- **GitHub Token Support**: 
  - Added the ability to use a GitHub token for authenticated API requests, improving access to private repository data.
  
- **Subscription Management**:
  - Introduced `subscription.json` to manage multiple repository subscriptions.
  - Users can enable/disable notifications and specify whether to be notified on new releases for each subscribed repository.

## Improvements
- Enhanced error handling for API requests.
- Improved modularity by separating configuration settings into `config.json`.

## Known Issues
- Ensure that the GitHub token has the necessary permissions for accessing the repositories.
- Subscription settings are currently limited to enabling/disabling notifications; future updates will include more granular control.

## Future Plans
- Add a user interface for managing subscriptions.
- Implement detailed logging for better monitoring and debugging.
- Explore additional features such as support for more notification channels.

## Get Involved
We welcome contributions! Please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file for more information on how to get involved.
