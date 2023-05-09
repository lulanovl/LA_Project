from scipy.spatial.distance import cosine
import numpy as np
import math



def cosine_similarity(x, y):
    dot_product = np.dot(x, y.T)
    norm_x = np.linalg.norm(x)
    norm_y = np.linalg.norm(y, axis=1)
    return dot_product / (norm_x * norm_y)



def argsort(seq):
    return sorted(range(len(seq)), key=seq.__getitem__)



class TruncatedSVD:
    def __init__(self, n_components):
        self.n_components = n_components
        self.U = None
        self.S = None
        self.Vt = None

    def fit_transform(self, X):
        # Step 1: Compute the Singular Value Decomposition of X
        U, S, Vt = self._svd(X)
        
        # Step 2: Reduce the dimensionality of X by truncating the SVD
        self.U = U[:, :self.n_components]
        self.S = S[:self.n_components]
        self.Vt = Vt[:self.n_components, :]
        X_reduced = np.dot(self.U, np.dot(np.diag(self.S), self.Vt))

        return X_reduced

    def _svd(self, X):
        # Compute the Singular Value Decomposition of X using the SVD algorithm
        # implemented in the numpy.linalg.svd() function.
        return np.linalg.svd(X)



class TfidfVectorizer:
    
    def __init__(self, analyzer='word'):
        self.idf = {}
        self.vocab = set()
        self.analyzer = analyzer

    def fit_transform(self, corpus):
        # Step 1: Tokenize the documents
        if self.analyzer == 'word':
            tokenized_corpus = [doc.lower().split() for doc in corpus]
        elif self.analyzer == 'char':
            tokenized_corpus = [list(doc.lower()) for doc in corpus]
        else:
            raise ValueError("Invalid analyzer type. Valid options are 'word' or 'char'.")
        
        # Step 2: Compute the term frequency (TF) for each word in each document
        tf = []
        for doc in tokenized_corpus:
            doc_tf = {}
            for word in doc:
                doc_tf[word] = doc_tf.get(word, 0) + 1
                self.vocab.add(word)
            tf.append(doc_tf)
        
        # Step 3: Compute the inverse document frequency (IDF) for each word in the corpus
        num_docs = len(tokenized_corpus)
        for word in self.vocab:
            doc_count = sum([1 for doc in tokenized_corpus if word in doc])
            self.idf[word] = math.log(num_docs / doc_count)

        # Step 4: Compute the TF-IDF score for each word in each document
        tf_idf = []
        for doc_tf in tf:
            doc_tf_idf = {}
            for word in doc_tf:
                doc_tf_idf[word] = doc_tf[word] * self.idf[word]
            tf_idf.append(doc_tf_idf)

        return tf_idf



def csr_matrix(data, indices, indptr, shape):
    """
    Create a CSR (Compressed Sparse Row) matrix from the given data, indices,
    indptr, and shape.
 
    Args:
        data (list): The non-zero values in the matrix, row-wise.
        indices (list): The column indices corresponding to the non-zero values
            in the data list, row-wise.
        indptr (list): The indices where each row starts in the data and indices
            lists.
        shape (tuple): The shape of the matrix, as a tuple of (num_rows, num_cols).
 
    Returns:
        csr_matrix: The CSR matrix created from the given data, indices, indptr,
        and shape.
    """
    num_rows, num_cols = shape
    num_nonzeros = len(data)
 
    # Initialize the row and column index arrays
    row_indices = [0] * num_nonzeros
    col_indices = [0] * num_nonzeros
 
    # Fill the row and column index arrays
    for i in range(num_rows):
        for j in range(indptr[i], indptr[i+1]):
            row_indices[j] = i
            col_indices[j] = indices[j]
 
    # Create the CSR matrix
    csr_data = data.copy()
    csr_row_indices = row_indices.copy()
    csr_indptr = indptr.copy()
    csr_shape = shape
    return (csr_data, csr_row_indices, csr_indptr, csr_shape)




def sorted(iterable, key=None, reverse=False):
    # Convert iterable to a list
    lst = [item for item in iterable]

    # Define the merge function
    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if key:
                if key(left[i]) < key(right[j]):
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            else:
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
        result += left[i:]
        result += right[j:]
        return result

    # Define the merge sort function
    def merge_sort(lst):
        if len(lst) <= 1:
            return lst
        mid = len(lst) // 2
        left = merge_sort(lst[:mid])
        right = merge_sort(lst[mid:])
        return merge(left, right)

    # Sort the list using the merge sort algorithm
    sorted_lst = merge_sort(lst)

    # Reverse the list if reverse=True
    if reverse:
        sorted_lst.reverse()

    return sorted_lst
 


