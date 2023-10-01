# Automated Patent Relevance System
 Help patent officers identify relevant prior patents when reviewing a new patent application using the U-CREAT model.
```mermaid
graph TD
    A[Patent Database] --> B[Preprocess & Extract Events]
    B --> C[Index Patents by Events]    
    D[New Patent Application] --> E[Extract Events]    
    F[Patent Event Index] --> G[Lookup Similar Events]    
    E --> G    
    G --> H[Rank Patents by Event Similarity]    
    H --> I[Return Top Similar Patent Results]
