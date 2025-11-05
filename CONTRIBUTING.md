# Contributing to Weather API Module

Thank you for considering contributing to this project! 🎉

## How to Contribute

### Reporting Bugs
- Check if the bug has already been reported in [Issues](../../issues)
- If not, create a new issue with a clear description and steps to reproduce

### Suggesting Enhancements
- Open an issue describing your suggested feature
- Explain why it would be useful

### Branching Strategy

We use a **Git Flow** approach:

- **`main`**: Production-ready code (protected)
- **`dev`**: Integration branch for features (default PR target)
- **`feature/*`**: New features or enhancements
- **`bugfix/*`**: Bug fixes
- **`hotfix/*`**: Urgent fixes for production

### Pull Requests

1. **Fork the repository** and create your feature branch from `dev`

   ```bash
   git checkout dev
   git pull origin dev
   git checkout -b feature/your-feature-name
   ```

   **Branch naming conventions:**
   - Features: `feature/add-temperature-conversion`
   - Bug fixes: `bugfix/fix-api-error-handling`
   - Hotfixes: `hotfix/critical-security-patch`

2. **Make your changes**
   - Write clear, commented code
   - Follow existing code style
   - Add tests if applicable

3. **Test your changes**

   ```bash
   pytest
   ```

4. **Commit your changes** with descriptive messages

   ```bash
   git commit -m "Add: temperature conversion feature"
   ```

   **Commit message conventions:**
   - `Add:` for new features
   - `Fix:` for bug fixes
   - `Update:` for improvements
   - `Refactor:` for code restructuring
   - `Docs:` for documentation changes

5. **Push to your fork**

   ```bash
   git push origin feature/your-feature-name
   ```

6. **Open a Pull Request to `dev`** (not `main`)
   - Provide a clear description of the changes
   - Reference any related issues (e.g., "Closes #42")
   - Ensure all CI checks pass
   - Wait for code review

7. **After approval**, your PR will be merged into `dev`
   - Releases to `main` are done periodically from `dev`

## Code Style

- Follow [PEP 8](https://pep8.org/) style guide
- Use meaningful variable and function names
- Add docstrings to functions
- Keep functions simple and focused

## Testing

- All tests must pass before merging
- Add tests for new features
- Run tests locally: `pytest test_weather.py -v`

## Questions?

Feel free to open an issue for any questions or discussions!

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
