import numpy as np
from random import shuffle

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  # pass
  N = X.shape[0]
  D = X.shape[1]
  C = W.shape[1]
  for i in range(N):
    f = np.dot(X[i], W)
    expsum = np.sum(np.exp(f - np.max(f)))
    loss += np.log(expsum) - f[y[i]] + np.max(f)
    dW += np.dot(X[i].reshape(D, 1), np.exp(f - np.max(f)).reshape(1, C)) / expsum
    dW[:, y[i]] -= X[i]
  
  loss = loss / N + 0.5 * reg * np.sum(W * W)
  dW = dW / N + reg * W
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  # pass
  N = X.shape[0]
  D = X.shape[1]
  C = W.shape[1]
  f = np.dot(X, W) # shape: (N, C)
  prob = np.exp(f - np.max(f, axis=1).reshape(N,1))
  expsum = np.sum(prob, axis=1) # shape: (N,)
  dW += np.dot(X.T, prob / expsum.reshape(N,1))
  mask = np.zeros((N, C))
  mask[range(N), y] = 1
  dW -= np.dot(X.T, mask)
  dW = dW / N + reg * W
  loss = np.log(expsum) - f[range(N),y] + np.max(f, axis=1)
  loss = np.sum(loss) / N + 0.5 * reg * np.sum(W * W)
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW

