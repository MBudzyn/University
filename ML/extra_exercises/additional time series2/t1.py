import pandas as pd
from scipy.io import arff
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import LeaveOneOut
from sklearn.metrics import f1_score, precision_score, recall_score, confusion_matrix, accuracy_score
import numpy as np


GLOBAL_K_VALUES = [3, 5, 7, 9, 11, 13, 15]
GLOBAL_TRAINING_PATH = 'data/Haptics_TRAIN.arff'
GLOBAL_TEST_PATH = 'data/Haptics_TEST.arff'
GLOBAL_WINDOW_SIZE = 10


def show_plt_with_info(x_label, y_label, title):
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    plt.close()


class Haptics:
    def __init__(self, data_path, test_path, k_values, all_metrics=True):
        self.metrics: dict[str, dict[int, int]] = {}
        self.data, self.meta = arff.loadarff(data_path)
        self.df = pd.DataFrame(self.data)
        self.all_metrics = all_metrics
        self.test_data, self.test_meta = arff.loadarff(test_path)
        self.test_df = pd.DataFrame(self.test_data)
        self.df['target'] = self.df['target'].apply(lambda x: x.decode('utf-8') if isinstance(x, bytes) else x)
        self.test_df['target'] = self.test_df['target'].apply(lambda x: x.decode('utf-8') if isinstance(x, bytes) else x)
        self.k_values = k_values
        self.confusion_matrices = {}

    def get_metrics(self):
        return self.metrics
    
    def print_basic_info(self):
        print(f"Number of data for each class: {self.df['target'].value_counts()}")
        print(f"Number of null values: {self.df.isnull().sum().sum()}")
        print(f"Number of classes: {len(self.df['target'].unique())}")
        print(f"Number of rows: {self.df.shape[0]}")
        print(f"Number of columns: {self.df.shape[1]}")
        print(f"Global min: {self.df.iloc[:, :-1].min().min()}")
        print(f"Global max: {self.df.iloc[:, :-1].max().max()}")
        print(self.df.head())
        print(self.df.describe())

    def plot_classes(self):
        classes = self.df['target'].unique()
        columns_len = len(self.df.columns) - 1
        plt.figure(figsize=(25, 5))
        for i, class_ in enumerate(classes):
            class_data = self.df[self.df['target'] == class_].drop(columns='target')
            plt.subplot(1, len(classes), i + 1)
            for j in range(len(class_data)):
                plt.plot(range(columns_len), class_data.iloc[j], alpha=0.5)
            plt.title(f'Class: {class_}')
            plt.xlabel('Time step')
            plt.ylabel('Amplitude')
        plt.tight_layout()
        plt.savefig('plots/classes_n_min_max_mean_median.png')
        plt.show()

    def drop_class_1(self):
        self.df = self.df[self.df['target'] != '1']

    def plot_classes_mean(self):
        classes = self.df['target'].unique()
        columns_len = len(self.df.columns) - 1
        colors = plt.get_cmap("tab10")
        plt.figure(figsize=(15, 5))

        for i, class_ in enumerate(classes):
            class_data = self.df[self.df['target'] == class_].drop(columns='target')
            avg_class_data = class_data.mean(axis=0)
            plt.plot(range(columns_len), avg_class_data, color=colors(i), lw=2, label=f'Class {class_}')

        show_plt_with_info('Time step', 'Amplitude', 'Mean of all classes')

    def plot_classes_median(self):
        classes = self.df['target'].unique()
        columns_len = len(self.df.columns) - 1
        colors = plt.get_cmap("tab10")
        plt.figure(figsize=(15, 5))

        for i, class_ in enumerate(classes):
            class_data = self.df[self.df['target'] == class_].drop(columns='target')
            median_class_data = class_data.median(axis=0)
            plt.plot(range(columns_len), median_class_data, color=colors(i), lw=2, label=f'Median Class {class_}')

        show_plt_with_info('Time step', 'Amplitude', 'Median of all classes')

    def plot_information(self):
        self.plot_classes()
        self.plot_classes_mean()
        self.plot_classes_median()
        self.range_of_values()

    def range_of_values(self):
        num_columns = len(self.df.columns) - 1
        step_size = 50
        classes = self.df.iloc[:, -1].unique()

        class_min_values = {}
        class_max_values = {}
        g_steps = []

        for cls in classes:
            class_df = self.df[self.df.iloc[:, -1] == cls]
            local_minima = []
            local_maxima = []
            steps = []

            for start in range(0, num_columns, step_size):
                end = min(start + step_size, num_columns)
                local_min = class_df.iloc[:, start:end].min().min()
                local_max = class_df.iloc[:, start:end].max().max()

                local_minima.append(local_min)
                local_maxima.append(local_max)
                steps.append(f"{start}-{end - 1}")

            class_min_values[cls] = local_minima
            class_max_values[cls] = local_maxima
            g_steps = steps

        plt.figure(figsize=(10, 6))
        for cls in classes:
            plt.plot(g_steps, class_min_values[cls], label=f'Class {cls} Min', marker='o')
        show_plt_with_info('Time Step Range', 'Value', 'Local Min Over Time for All Classes')

        plt.figure(figsize=(10, 6))
        for cls in classes:
            plt.plot(g_steps, class_max_values[cls], label=f'Class {cls} Max', marker='o')
        show_plt_with_info('Time Step Range', 'Value', 'Local Max Over Time for All Classes')

        plt.figure(figsize=(10, 6))
        for cls in classes:
            plt.plot(g_steps, class_min_values[cls], label=f'Class {cls} Min', marker='o')
            plt.plot(g_steps, class_max_values[cls], label=f'Class {cls} Max', marker='o')
        show_plt_with_info('Time Step Range', 'Value', 'Local Min and Max Over Time for All Classes')

    def test(self):
        accuracies = {}
        f1_scores = {}
        precisions = {}
        recalls = {}
        confusion_matrices = {}
        for k in self.k_values:
            print(f'\nTesting with k={k}')
            knn = KNeighborsClassifier(n_neighbors=k)
            knn.fit(self.df.iloc[:, :-1], self.df['target'])

            y_pred = knn.predict(self.test_df.iloc[:, :-1])
            y_true = self.test_df['target']

            accuracy = accuracy_score(y_true, y_pred)
            f1 = f1_score(y_true, y_pred, average='weighted', zero_division=0)
            precision = precision_score(y_true, y_pred, average='weighted', zero_division=0)
            recall = recall_score(y_true, y_pred, average="multilabel", zero_division=0)
            cm = confusion_matrix(y_true, y_pred, labels=self.df['target'].unique())
            accuracies[k] = accuracy
            f1_scores[k] = f1
            precisions[k] = precision
            recalls[k] = recall
            confusion_matrices[k] = cm

        self.confusion_matrices = confusion_matrices
        self.metrics = {
            'accuracy': accuracies,
            'f1_score': f1_scores,
            'precision': precisions,
            'recall': recalls,
        }
        self.plot_metrics()
        self.plot_confusion_matrix()

    def feature_engineering(self, window_size, replace=False):
        features_df = self.df.drop(columns=['target'])
        target = self.df['target']
        features_df_test = self.test_df.drop(columns=['target'])
        target_test = self.test_df['target']

        new_df_list = []
        new_df_list_test = []
        if not self.all_metrics:
            new_features = {"mean": np.mean, "median": np.median,
                            "min": np.min, "max": np.max}
        else:
            new_features = {"mean": np.mean, "median": np.median,
                            "variance": np.var,
                            "sum": np.sum,
                            "min": np.min, "max": np.max,
                            "standard_deviation": np.std}

        for i in range(0, len(features_df.columns), window_size):
            for feature_name, feature_func in new_features.items():
                feature_values = features_df.iloc[:, i:i + window_size].apply(feature_func, axis=1)
                new_df_list.append(feature_values.rename(f'{feature_name}_{i}'))
                feature_values = features_df_test.iloc[:, i:i + window_size].apply(feature_func, axis=1)
                new_df_list_test.append(feature_values.rename(f'{feature_name}_{i}'))

        new_features_df = pd.concat(new_df_list, axis=1)
        new_features_df_test = pd.concat(new_df_list_test, axis=1)

        if replace:
            new_features_df['target'] = target
            self.df = new_features_df
            new_features_df_test['target'] = target_test
            self.test_df = new_features_df_test
        else:
            self.df = pd.concat([features_df, new_features_df, target], axis=1)
            self.test_df = pd.concat([features_df_test, new_features_df_test, target_test], axis=1)

    def plot_metric(self, metric_name, ax):
        x = list(self.metrics[metric_name].keys())
        y = list(self.metrics[metric_name].values())
        ax.plot(x, y, marker='o')
        ax.set_title(f'{metric_name} vs k (neighbors)')
        ax.set_xlabel('k (neighbors)')
        ax.set_ylabel(metric_name)
        ax.grid(True)

        for i, value in enumerate(y):
            ax.text(x[i], y[i], f'{value * 100:.2f}%', ha='center', va='bottom', fontsize=9)

    def plot_metrics(self):
        plt.figure(figsize=(12, 8))

        for i, metric_name in enumerate(self.metrics.keys()):
            ax = plt.subplot(2, 2, i + 1)
            self.plot_metric(metric_name, ax)

        plt.tight_layout()
        plt.show()
        plt.close()

        self.plot_confusion_matrix()

    def plot_confusion_matrix(self):
        fig, axes = plt.subplots(3, 3, figsize=(15, 15))
        axes = axes.flatten()
        classes = self.df['target'].unique()
        tick_marks = np.arange(len(classes))

        for i, (k, cm) in enumerate(self.confusion_matrices.items()):
            cm_percent = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis] * 100
            cm_percent = np.round(cm_percent, 2)
            ax = axes[i]
            ax.imshow(cm_percent, interpolation='nearest', cmap=plt.get_cmap('Blues'))
            ax.set_title(f'Confusion Matrix (Percentages) for k={k}')
            ax.set_xticks(tick_marks)
            ax.set_yticks(tick_marks)
            ax.set_xticklabels(classes, rotation=45)
            ax.set_yticklabels(classes)
            ax.set_xlabel('Predicted label')
            ax.set_ylabel('True label')

            for m in range(cm.shape[0]):
                for n in range(cm.shape[1]):
                    ax.text(n, m, f'{cm_percent[m, n]}%',
                            ha='center', va='center',
                            color='black' if cm_percent[m, n] < 50 else 'white')

        plt.tight_layout()
        plt.show()
        plt.close()

    def loo_cv_knn(self):

        loo = LeaveOneOut()
        accuracies = {}
        f1_scores = {}
        precisions = {}
        recalls = {}
        confusion_matrices = {}
        n_classes = len(self.df['target'].unique())

        for k in self.k_values:
            final_cm = np.zeros((n_classes, n_classes))
            knn = KNeighborsClassifier(n_neighbors=k)
            y_true_all, y_pred_all = [], []

            for train_index, test_index in loo.split(self.df):
                X_train, X_test = self.df.iloc[train_index, :-1], self.df.iloc[test_index, :-1]
                y_train, y_test = self.df.iloc[train_index, -1], self.df.iloc[test_index, -1]
                knn.fit(X_train, y_train)
                y_pred = knn.predict(X_test)
                y_true_all.append(y_test.values[0])
                y_pred_all.append(y_pred[0])
                final_cm += confusion_matrix(y_test, y_pred, labels=self.df['target'].unique())

            confusion_matrices[k] = final_cm
            accuracies[k] = accuracy_score(y_true_all, y_pred_all)
            f1_scores[k] = f1_score(y_true_all, y_pred_all, average="weighted", zero_division=0)
            precisions[k] = precision_score(y_true_all, y_pred_all, average="weighted", zero_division=0)
            recalls[k] = recall_score(y_true_all, y_pred_all, average="weighted", zero_division=0)

        self.confusion_matrices = confusion_matrices
        self.metrics = {
            'accuracy': accuracies,
            'f1_score': f1_scores,
            'precision': precisions,
            'recall': recalls,
        }
        self.plot_metrics()


def run_on_raw_data(with_class_1=True):
    haptics = Haptics(GLOBAL_TRAINING_PATH, GLOBAL_TEST_PATH, GLOBAL_K_VALUES)
    if not with_class_1:
        haptics.drop_class_1()
    haptics.loo_cv_knn()
    return haptics


def run_on_fe_part_data(with_class_1=True):
    haptics = Haptics(GLOBAL_TRAINING_PATH, GLOBAL_TEST_PATH, GLOBAL_K_VALUES, all_metrics=False)
    if not with_class_1:
        haptics.drop_class_1()
    haptics.feature_engineering(GLOBAL_WINDOW_SIZE, replace=True)
    haptics.loo_cv_knn()
    return haptics


def run_on_feature_engineered_data(with_class_1=True):
    haptics = Haptics(GLOBAL_TRAINING_PATH, GLOBAL_TEST_PATH, GLOBAL_K_VALUES)
    if not with_class_1:
        haptics.drop_class_1()
    haptics.feature_engineering(GLOBAL_WINDOW_SIZE, replace=True)
    haptics.loo_cv_knn()
    return haptics


def run_on_mix_data(with_class_1=True):
    haptics = Haptics(GLOBAL_TRAINING_PATH, GLOBAL_TEST_PATH, GLOBAL_K_VALUES)
    if not with_class_1:
        haptics.drop_class_1()
    haptics.feature_engineering(GLOBAL_WINDOW_SIZE, replace=False)
    haptics.loo_cv_knn()
    return haptics


def plot_comparison(raw_metrics, fe_metrics, mix_metrics, fe_all_metrics):
    score_metrics = ['accuracy', 'f1_score', 'precision', 'recall']
    methods = {'Raw Data': raw_metrics, 'Feature-Engineered Part': fe_metrics,
               'Mixed Data': mix_metrics, 'Feature-Engineered All': fe_all_metrics}

    for metric in score_metrics:
        plt.figure(figsize=(10, 6))
        for method_name, method_metrics in methods.items():
            plt.plot(GLOBAL_K_VALUES, [method_metrics[metric][k] for k in GLOBAL_K_VALUES], label=method_name)

        plt.title(f'{metric.capitalize()} Comparison Across Methods')
        plt.xlabel('Number of Neighbors (k)')
        plt.ylabel(metric.capitalize())
        plt.legend()
        plt.grid(True)
        plt.show()


def compare_methods():
    raw_metrics = run_on_raw_data().get_metrics()
    fe_metrics = run_on_fe_part_data().get_metrics()
    fe_all_metrics = run_on_feature_engineered_data().get_metrics()
    mix_metrics = run_on_mix_data().get_metrics()
    plot_comparison(raw_metrics, fe_metrics, mix_metrics, fe_all_metrics)


def main():
    compare_methods()


if __name__ == '__main__':
    main()
