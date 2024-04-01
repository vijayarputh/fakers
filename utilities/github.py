import streamlit as st

def show_collaboration():
    st.subheader("Code Collaboration with GitHub")
    st.write("""
    GitHub is a platform widely used for code collaboration and version control. It allows multiple developers to work on the same project simultaneously without interfering with each other's changes.
    
    Here are the key steps involved in collaborating on code using GitHub:
    
    1. **Forking**: 
        - One developer forks the repository (creates a copy) to their GitHub account.
    2. **Cloning**: 
        - Each developer clones the repository to their local machine.
    3. **Branching**: 
        - Developers create separate branches to work on specific features or fixes.
    4. **Committing**: 
        - Developers make changes to the code and commit them to their branches.
    5. **Pull Request (PR)**: 
        - Once changes are ready, developers create a pull request to merge their branch into the main repository.
    6. **Reviewing**: 
        - Other team members review the code changes and provide feedback.
    7. **Merging**: 
        - After approval, the changes are merged into the main branch.
    """)

def show_refactoring():
    st.subheader("Code Refactoring")
    st.write("""
    Refactoring is the process of restructuring existing code without changing its external behavior. It aims to improve the code's readability, maintainability, and performance.
    
    Here are some common refactoring techniques:
    
    - **Extract Method**: 
        - Identify a code block that can be grouped into a separate method for better organization and reuse.
    - **Rename**: 
        - Rename variables, functions, or classes to better reflect their purpose.
    - **Simplify**: 
        - Simplify complex expressions or logic to make the code more understandable.
    - **Remove Duplication**: 
        - Eliminate duplicate code by creating reusable functions or using loops.
    - **Optimize**: 
        - Improve the performance of code by optimizing algorithms or data structures.
    """)

def main():
    st.title("Code Collaboration and Refactoring with GitHub")
    
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Code Collaboration", "Code Refactoring"])
    
    if page == "Code Collaboration":
        show_collaboration()
    elif page == "Code Refactoring":
        show_refactoring()

if __name__ == "__main__":
    main()
