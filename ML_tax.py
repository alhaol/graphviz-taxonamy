from graphviz import Digraph

taxonomy = Digraph(comment='MAchine Learning', engine='twopi')

taxonomy.attr(overlap='false')
taxonomy.attr(sep='0.5')
taxonomy.attr(nodesep='0.5')
taxonomy.attr(fontsize='20')
taxonomy.attr('node', fontname='Helvetica-Bold')

# add top-level "Machine Learning" node
machine_learning = 'Machine Learning'
taxonomy.node(machine_learning, machine_learning, shape='ellipse', style='filled', fillcolor='lightblue')

# set the size of the parent node to be smaller than the child nodes
taxonomy.attr('node', shape='ellipse', style='filled', fillcolor='lightblue')
taxonomy.attr('node', width='0.75', height='0.5')

# add top-level "Machine Learning" node
machine_learning = 'Machine Learning'
taxonomy.node(machine_learning, width='3', height='2')

# add nodes for each type and connect them to their corresponding ML category
supervised_learning = 'Supervised Learning'

taxonomy.node(supervised_learning, width='3', height='1.5')

supervised_classification = 'Classification'

taxonomy.node(supervised_classification, width='1.5', height='1')

supervised_regression = 'Regression'

taxonomy.node(supervised_regression, width='1.5', height='1')


unsupervised_learning = 'Unsupervised Learning'

taxonomy.node(unsupervised_learning, width='3', height='1.5')

unsupervised_clustering = 'Clustering'


taxonomy.node(unsupervised_clustering, width='2', height='0.75')
unsupervised_dim_reduction = 'Dimensionality Reduction'

taxonomy.node(unsupervised_dim_reduction, width='2', height='0.75')

unsupervised_anomaly_detection = 'Anomaly Detection'

taxonomy.node(unsupervised_anomaly_detection, width='2', height='0.75')
unsupervised_generative_models = 'Generative Models'

taxonomy.node(unsupervised_generative_models, width='2', height='0.75')

reinforcement_learning = 'Reinforcement Learning'

taxonomy.node(reinforcement_learning, width='3', height='1.5')
reinforcement_markov_decision = 'Markov Decision Processes'

taxonomy.node(reinforcement_markov_decision, width='2', height='0.75')
reinforcement_q_learning = 'Q-Learning'

taxonomy.node(reinforcement_q_learning, width='2', height='0.75')

reinforcement_policy_gradient = 'Policy Gradient Methods'

taxonomy.node(reinforcement_policy_gradient, width='2', height='0.75')

taxonomy.node(supervised_learning, supervised_learning, shape='ellipse', style='filled', fillcolor='lightblue')
taxonomy.node(supervised_classification, supervised_classification, shape='ellipse', style='filled', fillcolor='lightblue')
taxonomy.node(supervised_regression, supervised_regression, shape='ellipse', style='filled', fillcolor='lightblue')

taxonomy.node(unsupervised_learning, unsupervised_learning, shape='ellipse', style='filled', fillcolor='lightblue')
taxonomy.node(unsupervised_clustering, unsupervised_clustering, shape='ellipse', style='filled', fillcolor='lightblue')
taxonomy.node(unsupervised_dim_reduction, unsupervised_dim_reduction, shape='ellipse', style='filled', fillcolor='lightblue')
taxonomy.node(unsupervised_anomaly_detection, unsupervised_anomaly_detection, shape='ellipse', style='filled', fillcolor='lightblue')
taxonomy.node(unsupervised_generative_models, unsupervised_generative_models, shape='ellipse', style='filled', fillcolor='lightblue')

taxonomy.node(reinforcement_learning, reinforcement_learning, shape='ellipse', style='filled', fillcolor='lightblue')
taxonomy.node(reinforcement_markov_decision, reinforcement_markov_decision, shape='ellipse', style='filled', fillcolor='lightblue')
taxonomy.node(reinforcement_q_learning, reinforcement_q_learning, shape='ellipse', style='filled', fillcolor='lightblue')
taxonomy.node(reinforcement_policy_gradient, reinforcement_policy_gradient, shape='ellipse', style='filled', fillcolor='lightblue')

taxonomy.edge(machine_learning, supervised_learning)
taxonomy.edge(machine_learning, unsupervised_learning)
taxonomy.edge(machine_learning, reinforcement_learning)

taxonomy.edge(supervised_learning, supervised_classification)
taxonomy.edge(supervised_learning, supervised_regression)

taxonomy.edge(unsupervised_learning, unsupervised_clustering)
taxonomy.edge(unsupervised_learning, unsupervised_dim_reduction)
taxonomy.edge(unsupervised_learning, unsupervised_anomaly_detection)
taxonomy.edge(unsupervised_learning, unsupervised_generative_models)

taxonomy.edge(reinforcement_learning, reinforcement_markov_decision)
taxonomy.edge(reinforcement_learning, reinforcement_q_learning)
taxonomy.edge(reinforcement_learning, reinforcement_policy_gradient)

# add nodes for each wireless example and connect them to their corresponding type
predict_wireless_transmission = 'Predicting if a wireless transmission is legitimate or malicious'
predict_signal_strength = 'Predicting received signal strength at a particular location'
cluster_users = 'Clustering users based on their mobility patterns or signal characteristics'
reduce_data_features = 'Reducing the number of features in the data for compression or visualization'
detect_anomaly = 'Detecting unexpected network behavior'
synthesize_signals = 'Synthesizing realistic wireless signals'
design_comm_protocols = 'Designing wireless communication protocols'
optimize_resource_allocation = 'Optimizing resource allocation in wireless networks'
optimize_routing = 'Optimizing routing in wireless networks'

taxonomy.node(predict_wireless_transmission, predict_wireless_transmission, shape='rect', style='filled', fillcolor='lightblue')
taxonomy.node(predict_signal_strength, predict_signal_strength, shape='rect', style='filled', fillcolor='lightblue')
taxonomy.node(cluster_users, cluster_users, shape='rect', style='filled', fillcolor='lightblue')
taxonomy.node(reduce_data_features, reduce_data_features, shape='rect', style='filled', fillcolor='lightblue')
taxonomy.node(detect_anomaly, detect_anomaly, shape='rect', style='filled', fillcolor='lightblue')
taxonomy.node(synthesize_signals, synthesize_signals, shape='rect', style='filled', fillcolor='lightblue')
taxonomy.node(design_comm_protocols, design_comm_protocols, shape='rect', style='filled', fillcolor='lightblue')
taxonomy.node(optimize_resource_allocation, optimize_resource_allocation, shape='rect', style='filled', fillcolor='lightblue')
taxonomy.node(optimize_routing, optimize_routing, shape='rect', style='filled', fillcolor='lightblue')

taxonomy.edge(supervised_classification, predict_wireless_transmission)
taxonomy.edge(supervised_regression, predict_signal_strength)
taxonomy.edge(unsupervised_clustering, cluster_users)
taxonomy.edge(unsupervised_dim_reduction, reduce_data_features)
taxonomy.edge(unsupervised_anomaly_detection, detect_anomaly)
taxonomy.edge(unsupervised_generative_models, synthesize_signals)
taxonomy.edge(reinforcement_markov_decision, design_comm_protocols)
taxonomy.edge(reinforcement_q_learning, optimize_resource_allocation)
taxonomy.edge(reinforcement_policy_gradient, optimize_routing)

taxonomy.render('taxonomy_ML_categories', format='png')