import streamlit as st
import json
import os
from streamlit_shortcuts import button
from pathlib import Path

# Ensure data directory exists
Path("./data").mkdir(exist_ok=True)

# App title and layout configuration
st.set_page_config(layout="wide", page_title="Simple Annotation Tool")
st.title("Simple Annotation Tool")


# Load conversations
@st.cache_data
def load_conversations():
    try:
        with open("./data/conversations.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        st.error("conversations.json file not found in ./data directory!")
        return []


# Initialize or load labels
def load_labels():
    labels_file = "./data/labels.jsonl"
    labels = {}
    if os.path.exists(labels_file):
        with open(labels_file, mode="r") as f:
            for line in f:
                if line.strip():
                    item = json.loads(line)
                    labels[item["query_id"]] = item["label"]
    return labels


# Save label
def save_label(conversation, label_value):
    labels_file = "./data/labels.jsonl"
    label_data = {
        "query_id": conversation["query_id"],
        "query": conversation["query"],
        "matching_document": conversation["matching_document"],
        "label": label_value,
    }

    # Append to the jsonl file
    with open(labels_file, mode="a") as f:
        f.write(json.dumps(label_data) + "\n")

    # Update session state
    st.session_state.labels[conversation["query_id"]] = label_value
    st.session_state.next_item = True


# Label functions
def label_artifact():
    if st.session_state.current_index < len(st.session_state.conversations):
        save_label(
            st.session_state.conversations[st.session_state.current_index], "artifact"
        )


def label_no_artifact():
    if st.session_state.current_index < len(st.session_state.conversations):
        save_label(
            st.session_state.conversations[st.session_state.current_index],
            "not_artifact",
        )


# Navigation functions
def prev_item():
    if st.session_state.current_index > 0:
        st.session_state.current_index -= 1


def next_item():
    if st.session_state.current_index < len(st.session_state.conversations) - 1:
        st.session_state.current_index += 1


# Initialize session state
if "current_index" not in st.session_state:
    st.session_state.current_index = 0
    st.session_state.conversations = load_conversations()
    st.session_state.labels = load_labels()
    st.session_state.next_item = False

# Initialize button counter for streamlit_shortcuts
if "button_key_counter" not in st.session_state:
    st.session_state.button_key_counter = 0

# Handle navigation from previous interactions
if st.session_state.next_item:
    if st.session_state.current_index < len(st.session_state.conversations) - 1:
        st.session_state.current_index += 1
    st.session_state.next_item = False

# Progress info in sidebar
with st.sidebar:
    st.header("Annotation Progress")
    total = len(st.session_state.conversations)
    labeled = len(st.session_state.labels)
    remaining = total - labeled

    st.write(f"**Labeled:** {labeled}/{total}")
    st.write(f"**Remaining:** {remaining}")
    st.progress(labeled / total if total > 0 else 0)

    st.subheader("Keyboard Shortcuts")
    st.write("**Ctrl+E:** Artifact")
    st.write("**Ctrl+R:** No Artifact")
    st.write("**Ctrl+P:** Previous")
    st.write("**Ctrl+N:** Next")

# Main display area - simple layout with plain text
if st.session_state.conversations:
    if st.session_state.current_index < len(st.session_state.conversations):
        conversation = st.session_state.conversations[st.session_state.current_index]

        # Simple item indicator at the top
        status_row = st.columns([3, 1])
        with status_row[0]:
            st.text(
                f"Item {st.session_state.current_index + 1} of {len(st.session_state.conversations)}"
            )
        with status_row[1]:
            already_labeled = conversation["query_id"] in st.session_state.labels
            if already_labeled:
                label = st.session_state.labels[conversation["query_id"]]
                st.text(f"[LABELED: {label}]")

        # Clear keyboard shortcuts reminder at the top
        st.markdown("**Ctrl+E**: Mark as Artifact | **Ctrl+R**: Mark as No-Artifact")
        st.markdown("---")

        # Show query | document in a clean side-by-side layout
        cols = st.columns(2)

        with cols[0]:
            st.text("QUERY:")
            st.text_area(
                "",
                conversation["query"],
                height=100,
                disabled=True,
                key="query_field",
                label_visibility="collapsed",
            )

        with cols[1]:
            st.text("DOCUMENT:")
            st.text_area(
                "",
                conversation["matching_document"],
                height=300,
                disabled=True,
                key="doc_field",
                label_visibility="collapsed",
            )

        # Simple button row at the bottom
        button_cols = st.columns([1, 1, 3])
        with button_cols[0]:
            if button("⭐️ Artifact", "ctrl+e", label_artifact, hint=True):
                label_artifact()
        with button_cols[1]:
            if button("❌ No-Artifact", "ctrl+r", label_no_artifact, hint=True):
                label_no_artifact()
    else:
        st.success("All items have been processed!")
else:
    st.error(
        "No data available. Please ensure your conversations.json file is in the ./data directory."
    )
