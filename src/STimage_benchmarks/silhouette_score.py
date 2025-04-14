import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import silhouette_samples, silhouette_score


class SilhouetteAnalyzer:
    def __init__(self, X, y):
        self.X = X.to_numpy()
        self.y = y.to_numpy()
        self.cluster_labels = self.y.flatten()
        self.n_clusters = self.y.max() + 1
        self.silhouette_avg = None
        self.sample_silhouette_values = None

    
    def compute_silhouette_score(self):
        # Compute the silhouette scores for each sample
        self.sample_silhouette_values = silhouette_samples(self.X, self.cluster_labels)
        # Compute the average silhouette score
        self.silhouette_avg = silhouette_score(self.X, self.cluster_labels)
        return self.silhouette_avg
    
    def plot_silhouette(self):
        """Plot the silhouette analysis and cluster visualization."""
        if self.silhouette_avg is None or self.sample_silhouette_values is None:
            raise ValueError("Silhouette scores have not been calculated. Call `calculate_silhouette_score` first.")

        fig, (ax1, ax2) = plt.subplots(1, 2)
        fig.set_size_inches(18, 7)

        # The 1st subplot is the silhouette plot
        ax1.set_xlim([-1, 1])
        ax1.set_ylim([0, len(self.X) + (self.n_clusters + 1) * 10])

        y_lower = 10
        for i in range(self.n_clusters):
            # Aggregate the silhouette scores for samples belonging to cluster i
            ith_cluster_silhouette_values = self.sample_silhouette_values[self.cluster_labels == i]
            ith_cluster_silhouette_values.sort()

            size_cluster_i = ith_cluster_silhouette_values.shape[0]
            y_upper = y_lower + size_cluster_i

            color = cm.nipy_spectral(float(i) / self.n_clusters)
            ax1.fill_betweenx(
                np.arange(y_lower, y_upper),
                0,
                ith_cluster_silhouette_values,
                facecolor=color,
                edgecolor=color,
                alpha=0.7,
            )

            # Label the silhouette plots with their cluster numbers at the middle
            ax1.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))

            # Compute the new y_lower for next plot
            y_lower = y_upper + 10

        ax1.set_title("The silhouette plot for the various clusters.")
        ax1.set_xlabel("The silhouette coefficient values")
        ax1.set_ylabel("Cluster label")
        ax1.axvline(x=self.silhouette_avg, color="red", linestyle="--")
        ax1.set_yticks([])
        ax1.set_xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1])

        # 2nd Plot showing the actual clusters formed
        colors = cm.nipy_spectral(self.cluster_labels.astype(float) / self.n_clusters)
        ax2.scatter(
            self.X[:, 0], self.X[:, 1], marker=".", s=30, lw=0, alpha=0.7, c=colors, edgecolor="k"
        )

        # Labeling the clusters
        centers = np.array([self.X[self.cluster_labels == i].mean(axis=0) for i in range(self.n_clusters)])
        ax2.scatter(
            centers[:, 0],
            centers[:, 1],
            marker="o",
            c="white",
            alpha=1,
            s=200,
            edgecolor="k",
        )

        for i, c in enumerate(centers):
            ax2.scatter(c[0], c[1], marker="$%d$" % i, alpha=1, s=50, edgecolor="k")

        ax2.set_title("The visualization of the clustered data.")
        ax2.set_xlabel("Feature space for the 1st feature")
        ax2.set_ylabel("Feature space for the 2nd feature")

        plt.suptitle(
            "Silhouette analysis for clustering on sample data with n_clusters = %d"
            % self.n_clusters,
            fontsize=14,
            fontweight="bold",
        )

        plt.show()

    