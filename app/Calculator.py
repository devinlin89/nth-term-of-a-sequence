import streamlit as st

from nth_term import find_nth_term, parse_sequence
from nth_term.formulas import COEFFICIENT_NAMES, GENERAL_FORMULAS
from nth_term.models import SequenceData, SequenceType


def _apply_styles() -> None:
    """Apply custom styles to the application."""

    st.markdown(
        """
        <style>
        .st-key-sequence-type-card,
        .st-key-general-form-card,
        .st-key-number-of-terms-card {
            min-height: 150px;
            padding: 1rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def _display_summary(
    sequence: SequenceData,
    sequence_type: SequenceType,
) -> None:
    """Display summary information about the sequence."""

    col1, col2, col3 = st.columns([1, 1.5, 1])

    with col1:
        with st.container(border=True, key="sequence-type-card"):
            st.caption("Sequence Type")
            st.markdown(
                f"### {sequence_type.value.capitalize()}"
            )

    with col2:
        with st.container(border=True, key="general-form-card"):
            st.caption("General Form")
            st.latex(GENERAL_FORMULAS[sequence_type])

    with col3:
        with st.container(border=True, key="number-of-terms-card"):
            st.caption("Number of Terms")
            st.markdown(f"### {len(sequence)}")


def _display_formula(formula) -> None:
    """Display the calculated nth-term formula."""

    with st.container(border=True):
        st.caption("Nth-Term Formula")
        st.latex(rf"U_n = {formula}")


def _display_coefficients(
    sequence_type: SequenceType,
    coefficients: tuple,
) -> None:
    """Display the coefficients of the nth-term formula."""

    with st.container(border=True):
        st.caption("Coefficients")

        names = COEFFICIENT_NAMES[sequence_type]
        columns = st.columns(len(names))

        for column, name, value in zip(
            columns,
            names,
            coefficients,
        ):
            with column:
                st.latex(rf"{name} = {value}")


def _display_result(sequence: SequenceData, result) -> None:
    """Display the result of the sequence calculation."""

    sequence_type = result.sequence_type

    with st.container(border=True):
        st.subheader("Result")

        _display_summary(sequence, sequence_type)

        st.write("")

        _display_formula(result.formula)

        st.write("")

        _display_coefficients(
            sequence_type,
            result.coefficients,
        )


def _calculate_and_display(sequence_input: str) -> None:
    """Calculate and display the nth-term formula for user input."""

    if not sequence_input.strip():
        st.error("Please enter a sequence.")
        return

    try:
        sequence = parse_sequence(sequence_input)
        result = find_nth_term(sequence)
    except ValueError as error:
        st.error(str(error))
        return

    if result.formula is None:
        st.warning(
            """
            This sequence could not be identified as a supported sequence type.

            Possible reasons:
            - The sequence is too short to determine its type.
            - The sequence does not follow a linear, quadratic, cubic,
            or exponential pattern.
            - The sequence contains values that do not satisfy the
            requirements of the supported sequence types.
            """
        )
        return

    _display_result(sequence, result)


def main() -> None:
    """Run the Streamlit application."""

    st.set_page_config(
        page_title="Nth Term of a Sequence",
        page_icon="📐",
        layout="centered",
    )

    _apply_styles()

    st.title("Nth Term of a Sequence")
    st.write(
        "Enter a sequence to determine its type and calculate "
        "its nth-term formula."
    )

    sequence_input = st.text_input(
        "Sequence",
        placeholder="e.g. 2, 5, 8, 11, 14",
    )

    if st.button(
        "Find nth term",
        type="primary",
        use_container_width=True,
    ):
        _calculate_and_display(sequence_input)


if __name__ == "__main__":
    main()